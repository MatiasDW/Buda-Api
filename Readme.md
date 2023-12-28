# Buda-Api

## Introduction
Spread API is a REST API designed and implemented as part of Buda.com's initiatives to facilitate interaction with cryptocurrency markets. This API allows users to calculate and retrieve the spread of markets on Buda.com and manage spread alerts for continuous monitoring.

### Prerequisites
- Python 3.8 or higher. I used Python 3.11 with pip version 23.2.1
- pip for managing Python packages.

### Features
- Calculate the spread for any market on Buda.com.
- Retrieve spreads for all markets in a single call.
- Manage and query alert spreads for continuous monitoring.

## Installation and Setup
**Clone the Repository:**
git clone https://github.com/MatiasDW/Buda-Api
cd spread-api

## Install Dependencies:
pip install -r requirements.txt

## Environment Variables:
- Set up necessary environment variables according to your local or production setup.

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

# Docker Setup and Usage

### Building the Docker Container
- To build a Docker container for this application, ensure you have Docker installed and running on your system. Then, execute the following command from the root of the project:

docker build -t buda-api .

- This command builds a Docker image named buda-api based on the instructions in your Dockerfile.

# Running the Application in a Container
Once the image is built, you can run the application in a Docker container. To do so, use the following command:
docker run -p 5000:5000 buda-api

## Notes
- Ensure the port number specified in the docker run command matches the port on which your application is set to run.
For any changes in the code or dependencies, you'll need to rebuild the image for them to take effect in the container.

# API Reference

- GET /spread/<market_id>
Retrieves the spread for the specified market.

URL Parameters:

market_id: The ID of the market for which to calculate the spread.
Response:

A JSON object containing the market ID and the spread:

{
    "market_id": "BTC-CLP",
    "spread": 10000
}
Errors:

400: No bids or asks for the specified market.
500: Unable to calculate spread.

- POST /set_alert
Sets the alert spread value.

Request Body:

A JSON object containing the alert spread:

{
    "spread": 10000
}
Response:

A JSON object containing the new alert spread value:

{
    "alert_set_to": 10000
}

- GET /check_alert/<market_id>
Checks if the current spread for the specified market is greater than the alert spread.

URL Parameters:

market_id: The ID of the market for which to check the alert.
Response:

A JSON object containing the market ID, the current spread, and whether the alert is triggered:

{
    "market_id": "BTC-CLP",
    "spread": 10000,
    "alert": false
}
Errors:

400: Alert spread is not set.
500: Unable to calculate spread.

## Examples
You can use curl to make requests to the API. Here's an example of how to set the alert spread:

curl -X POST -H "Content-Type: application/json" -d '{"spread":10000}' http://localhost:5000/set_alert
Replace localhost:5000 with your server's address and port.

# Environment Variables
## The application uses the following environment variables:
- API_KEY: Your Buda.com API key. This is used to authenticate with the Buda.com API.
- API_SECRET: Your Buda.com API secret. This is used to authenticate with the Buda.com API.

# FAQ
## How can I change the port on which the API runs?
- You can modify the configuration file or set an environment variable to specify a different port.

## Where can I find more information about the available markets?
- Visit the official Buda.com documentation for an updated list of markets and their IDs.

# License
- This project is under the MIT License - see the LICENSE.md file for details.

# Contact
- For support, questions, or collaboration, you can reach me at matiasdw8@gmail.com or https://github.com/MatiasDW

# Contributions
- Contributions are welcome! Here's how you can contribute to this project:

- Reporting Bugs: Open an issue in the GitHub repository describing the bug.
- Suggesting Features: Open an issue in the GitHub repository describing the new feature.
- Submitting Pull Requests: If you've fixed a bug or added a new feature, you can submit a pull request. Please ensure your code follows the existing style and all tests pass