import os
from flask import jsonify
import requests

ALERT_SPREAD = None

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
    # structure for setting an alert
    global ALERT_SPREAD 
    ALERT_SPREAD = request.json.get('spread')
    return jsonify({'alert_set_to': ALERT_SPREAD})

def check_alert(market_id):
    spread_info, status_code = calculate_spread(market_id)
    if status_code != 200:
        return {'error': 'Unable to calculate spread'}, 500
    if ALERT_SPREAD is None:
        return {'error': 'Alert spread is not set'}, 400
    current_spread = spread_info['spread']
    alert_triggered = current_spread > ALERT_SPREAD
    return {'market_id': market_id, 'spread': current_spread, 'alert': alert_triggered}, 200
