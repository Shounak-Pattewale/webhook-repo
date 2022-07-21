import os

# from flask import Flask
# from flask_restful import Api

import const as const
from app import app
# Import Errors
from app.basic_errors import basic_errors
# from api.routes import initialize_routes
from db import initialize_db, db

# Initializing routes
# collective_errors = {**basic_errors}
# api = Api(app, errors=collective_errors)

# Initialize database connection
initialize_db(app)

# Initializing routes
# initialize_routes(api)
