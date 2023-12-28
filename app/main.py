from flask import Flask
from routes import define_routes

app = Flask(__name__)

# Define the end points of the app 
define_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
