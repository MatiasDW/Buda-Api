import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

import unittest
import json
from app.main import app
from app.routes import define_routes


class APITestCase(unittest.TestCase):
    # Set up a test client for the application for use in the test cases.
    def setUp(self):
        self.app = app.test_client()

    # Test the '/spread/btc-clp' endpoint to ensure it calculates the spread correctly.
    def test_calculate_spread(self):
        response = self.app.get('/spread/btc-clp')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('spread', data)

    # Test the '/set_alert' endpoint to ensure it sets a spread alert successfully.
    def test_set_alert(self):
        response = self.app.post('/set_alert', json={'spread': 1000})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('alert_set_to', data)

    # Test the '/check_alert/btc-clp' endpoint to verify it checks the spread alert correctly.
    def test_check_alert(self):
        self.app.post('/set_alert', json={'spread': 1000}) # Setting up an alert to check.
        response = self.app.get('/check_alert/btc-clp')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('alert', data)

if __name__ == '__main__':
    unittest.main()