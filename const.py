import os

# environments
flask_env_dev = "development"
flask_env_testing = "testing"
flask_env_production = "production"

# response message key
response_message_key = "message"
response_status_key = "status"

# Http response statuses codes

# successful responses - 2xx
status_ok_200 = 200
status_created_201 = 201

# client side errors - 4xx
status_badrequest_400 = 400
status_unauthorized_401 = 401
status_already_exists_403 = 403
status_notfound_404 = 404

# server side errors
status_internal_server_error_500 = 500

records_per_page = int(os.environ.get('RECORDS_PER_PAGE'))
pagination_btn_length = int(os.environ.get('PAGINATION_BTN_LENGTH'))