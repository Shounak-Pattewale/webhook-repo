from api import app
from db import initialize_db

# Initialize database connection
initialize_db(app)
