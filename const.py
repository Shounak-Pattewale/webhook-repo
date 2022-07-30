import os

# environments
FLASK_ENV_DEV = "development"
FLASK_ENV_TESTING = "testing"
FLASK_ENV_PRODUCTION = "production"

# response message key
RESPONSE_MESSAGE_KEY = "message"
RESPONSE_STATUS_KEY = "status"

# HTTP response statuses codes

# successful responses - 2xx
STATUS_OK_200 = 200
STATUS_CREATED_201 = 201

# client side errors - 4xx
STATUS_BADREQUEST_400 = 400
STATUS_UNAUTHORIZED_401 = 401
STATUS_ALREADY_EXISTS_403 = 403
STATUS_NOTFOUND_404 = 404

# server side errors
STATUS_INTERNAL_SERVER_ERROR_500 = 500

# pagination
RECORDS_PER_PAGE = int(os.environ.get('RECORDS_PER_PAGE'))
PAGINATION_BTN_LENGTH = int(os.environ.get('PAGINATION_BTN_LENGTH'))