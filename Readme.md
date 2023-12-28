# Spread API

## Introduction
Spread API is a REST API designed and implemented as part of Buda.com's initiatives to facilitate interaction with cryptocurrency markets. This API allows users to calculate and retrieve the spread of markets on Buda.com and manage spread alerts for continuous monitoring.

### Prerequisites
- Python 3.8 or higher.
- pip for managing Python packages.

### Features
- Calculate the spread for any market on Buda.com.
- Retrieve spreads for all markets in a single call.
- Manage and query alert spreads for continuous monitoring.

## Installation and Setup
**Clone the Repository:**
bash
git clone [Repository URL]
cd spread-api

## Install Dependencies:
pip install -r requirements.txt

## Environment Variables:
Set up necessary environment variables according to your local or production setup.

# Usage
## Start the aplication 
python app/main.py
### This will start the server on the defined port (default is 5000).

# Endpoints
## Get Spread for a Specific Market:
GET /spread/<market_id>
### market_id: ID of the market for which you want to calculate the spread.

## Get Spread for All Markets:
GET /spread/all

## Set and Query Alert Spread:
POST /alert/spread
### Send the desired alert spread value in the request body.

# Usage
## Query Spread for Bitcoin in Buda (BTC-CLP).
curl http://localhost:5000/spread/BTC-CLP

## Set Spread Alert:
curl -X POST http://localhost:5000/alert/spread -d '{"alert_value": 5000}'

# Project Structure
- app/: Contains the source code.
-- main.py: The entry point of the application.
-- routes.py: Defines the API endpoints and logic.
-- utils.py: Utility functions.
- tests/: Automated tests.
-- test_api.py: Tests to validate the API functionality.

# Automated Tests
## Run Tests:
python -m unittest tests/test_api.py

# FAQ
## How can I change the port on which the API runs?
### You can modify the configuration file or set an environment variable to specify a different port.

## Where can I find more information about the available markets?
### Visit the official Buda.com documentation for an updated list of markets and their IDs.

# License
## This project is under the MIT License - see the LICENSE.md file for details.

# Contact
## For support, questions, or collaboration, you can reach me at matiasdw8@gmail.com or https://github.com/MatiasDW

# Contributions
### Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.