import const as const


class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class NoAuthorizationError(Exception):
    pass


basic_errors = {
    "InternalServerError": {
        const.RESPONSE_MESSAGE_KEY: "Something went wrong",
        const.RESPONSE_STATUS_KEY: const.STATUS_INTERNAL_SERVER_ERROR_500
    },
    "SchemaValidationError": {
        const.RESPONSE_MESSAGE_KEY: "Request is missing required fields",
        const.RESPONSE_STATUS_KEY: const.STATUS_BADREQUEST_400
    },
    "NoAuthorizationError": {
        const.RESPONSE_MESSAGE_KEY: "Missing Authorization",
        const.RESPONSE_STATUS_KEY: const.STATUS_UNAUTHORIZED_401
    }
}
