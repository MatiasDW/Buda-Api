import requests
from flask import jsonify, request
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
        market_id = "btc-clp"  # real market ID
        spread_info, status_code = calculate_spread(market_id)  # Unpack the tuple

        #Chek the status code to extract data.
        if status_code == 200:
            spread_data = spread_info.json  # Access to .json metod to obtain data.
            return f"El spread para el mercado {market_id} es {spread_data['spread']} CLP"
        else:
            return "No se pudo obtener el spread para el mercado especificado."



  