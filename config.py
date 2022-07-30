import os

# Default configurations are common across environments
class DefaultConfig(object):
    # Machine Configuration
    HOST_MACHINE_IP = os.environ.get('HOST_MACHINE_IP')
    HOST_MACHINE_PORT = os.environ.get('HOST_MACHINE_PORT')

    # Debug Configuration
    DEBUG = os.environ.get('DEBUG')

    # Database Configuration
    DB_URI = os.environ.get('DB_URI')
    DB_NAME = os.environ.get('DB_NAME')
    DB_PORT = os.environ.get('DB_PORT')
    DB_CONNECTION_TIMEOUT = os.environ.get('DB_CONNECTION_TIMEOUT')