from nasse.exceptions import NasseException


class DatabaseDisabled(NasseException):
    STATUS_CODE = 501
    MESSAGE = "The database is currently disabled on the server"
    EXCEPTION_NAME = "DATABASE_DISABLED"
    LOG = False


class Forbidden(NasseException):
    STATUS_CODE = 403
    MESSAGE = "You do not have the rights to access this endpoint"
    EXCEPTION_NAME = "FORBIDDEN"
    LOG = False


class NotFound(NasseException):
    STATUS_CODE = 404
    MESSAGE = "We couldn't find the resource you were looking for"
    EXCEPTION_NAME = "NOT_FOUND"
    LOG = False
