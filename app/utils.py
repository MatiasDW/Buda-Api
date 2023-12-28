import os
from flask import jsonify
import requests
import json

ALERT_SPREAD_FILE = 'alert_spread.json'

# Load environment variables
API_KEY = os.getenv('BUDA_API_KEY')
API_SECRET = os.getenv('BUDA_API_SECRET')
BUDA_BASE_URL = "https://www.buda.com/api/v2/"

def calculate_spread(market_id):
    order_book_url = f"{BUDA_BASE_URL}markets/{market_id}/order_book"
    response = requests.get(order_book_url)

    if response.status_code == 200:
        order_book = response.json()['order_book']
        if order_book['bids'] and order_book['asks']:  # Check if 'bids' and 'asks' lists are not empty
            best_bid = float(order_book['bids'][0][0])  # Highest buy order
            best_ask = float(order_book['asks'][0][0])  # Lowest sell order
            spread = best_ask - best_bid  # Calculate spread
            print(f'Spread for market {market_id}: {spread}')
            return {'market_id': market_id, 'spread': spread}, 200
        else:
            return {'error': f'No bids or asks for market {market_id}'}, 400
    else:
        return {'error': 'Unable to fetch order book'}, response.status_code

def set_alert(request):
    alert_spread = request.json.get('spread')
    with open(ALERT_SPREAD_FILE, 'w') as f:
        json.dump({'alert_spread': alert_spread}, f)
    return jsonify({'alert_set_to': alert_spread})

def check_alert(market_id):
    try:
        with open(ALERT_SPREAD_FILE, 'r') as f:
            alert_spread = json.load(f)['alert_spread']
    except FileNotFoundError:
        return {'error': 'Alert spread is not set'}, 400

    spread_info, status_code = calculate_spread(market_id)
    if status_code != 200:
        return {'error': 'Unable to calculate spread'}, 500
    current_spread = spread_info['spread']
    alert_triggered = current_spread > alert_spread
    return {'market_id': market_id, 'spread': current_spread, 'alert': alert_triggered}, 200
