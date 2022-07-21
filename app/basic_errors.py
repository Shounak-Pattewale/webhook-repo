import const as const

class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class NoAuthorizationError(Exception):
    pass

basic_errors = {
    "InternalServerError": {
        const.response_message_key: "Something went wrong",
        const.response_status_key: const.status_internal_server_error_500
    },
    "SchemaValidationError": {
        const.response_message_key: "Request is missing required fields",
        const.response_status_key: const.status_badrequest_400
    },
    "NoAuthorizationError": {
        const.response_message_key: "Missing Authorization",
        const.response_status_key: const.status_unauthorized_401
    }
}
