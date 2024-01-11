import requests
from flask import jsonify, request, Response
from utils import calculate_spread as calculate_spread_util, set_alert as set_alert_util, check_alert as check_alert_util

def define_routes(app):

    @app.route('/spread/<market_id>', methods=['GET'])
    def calculate_spread(market_id):
        spread_info, status_code = calculate_spread_util(market_id)
        return jsonify(spread_info), status_code

    @app.route('/set_alert', methods=['POST'])
    def set_alert():
        return set_alert_util(request)

    @app.route('/check_alert/<market_id>', methods=['GET'])
    def check_alert(market_id):
        return check_alert_util(market_id)
    
    @app.route('/')
    def home():
        response = requests.get('https://www.buda.com/api/v2/markets')
        markets = response.json()
        spreads = []

        for market in markets['markets']:
            market_id = market['id']
            spread_info, status_code = calculate_spread(market_id)
            if status_code == 200:
                spread_data = spread_info.json
                spreads.append(f"El spread para el mercado {market_id} es {spread_data['spread']} CLP")
            else:
                spreads.append(f"No se pudo obtener el spread para el mercado {market_id}")

        return Response("<br>".join(spreads), mimetype='text/html')

    # @app.route('/test_set_alert', methods=['GET'])
    # def test_set_alert():
    #     return set_alert_util({"json": {"spread": 10000}})