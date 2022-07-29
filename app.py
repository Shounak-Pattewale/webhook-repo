from flask import Flask
from db import initialize_db
from config import DefaultConfig

# Blueprint imports
from api import api
from views import views

# Initializing app
app = Flask(__name__)

# Registering blueprints
app.register_blueprint(api)
app.register_blueprint(views)

# Load default configuration for the application (common across environments)
app.config.from_object(DefaultConfig)

app.config['MONGODB_SETTINGS'] = {
    'db': app.config['DB_NAME'],
    'host': app.config['DB_URI'],
    'connect': False
}

# Initializing database connection
initialize_db(app)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])