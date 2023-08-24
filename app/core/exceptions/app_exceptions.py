from typing import Any, Union

from fastapi.logger import logger


class AppExceptionCase(Exception):
    """
    base exception to be raised by the application
    """

    def __init__(self, status_code: int, error_message: Any, context=None):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.error_message = error_message
        self.context = context
        logger.critical(self.context) if self.context else None

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code = {self.status_code} - error_message = {self.error_message}>"
        )


class AppException:
    """
    the various exceptions that will be raised by the application
    """

    class OperationError(AppExceptionCase):
        """
        exception to catch errors caused by failed operations
        :param error_message: the message return from request
        :param context: other message suitable for troubleshooting errors
        """

        def __init__(self, error_message, context=None):
            status_code = 400
            super().__init__(status_code, error_message, context=context)

    class InternalServerError(AppExceptionCase):
        """
        exception to catch errors caused by servers inability to process an operation
        :param error_message: the message return from request
        :param context: other message suitable for troubleshooting errors
        """

        def __init__(self, error_message, context=None):
            status_code = 500
            super().__init__(status_code, error_message, context=context)

    class ResourceExists(AppExceptionCase):
        """
        exception to catch errors caused by resource duplication
        :param error_message: the message return from request
        :param context: other message suitable for troubleshooting errors
        """

        def __init__(self, error_message, context=None):
            status_code = 400
            super().__init__(status_code, error_message, context=context)

    class NotFoundException(AppExceptionCase):
        def __init__(self, error_message: Union[str, None], context=None):
            """
            exception to catch errors caused by resource nonexistence
            :param error_message: the message return from request
            :param context: other message suitable for troubleshooting errors
            """

            status_code = 404
            super().__init__(status_code, error_message, context=context)

    class Unauthorized(AppExceptionCase):
        def __init__(self, error_message, context=None):
            """
            exception to catch errors caused by illegitimate operation
            :param error_message: the message return from request
            :param context: other message suitable for troubleshooting errors
            """

            status_code = 401
            super().__init__(status_code, error_message, context=context)

    class ValidationException(AppExceptionCase):
        """
        exception the catch errors caused by invalid data
        :param error_message: the message return from request
        :param context: other message suitable for troubleshooting errors
        """

        def __init__(self, error_message, context=None):
            status_code = 400
            super().__init__(status_code, error_message, context=context)

    class BadRequest(AppExceptionCase):
        def __init__(self, error_message, context=None):
            """
            exception to catch errors caused by invalid requests
            :param error_message: the message return from request
            :param context: other message suitable for troubleshooting errors
            """

            status_code = 400
            super().__init__(status_code, error_message, context=context)

    class InvalidTokenException(AppExceptionCase):
        def __init__(self, error_message, context=None):
            """
            exception to catch errors caused by invalid jwt
            :param error_message: the message return from request
            :param context: other message suitable for troubleshooting errors
            """

            status_code = 400
            super().__init__(status_code, error_message, context=context)

    class ServiceRequestException(AppExceptionCase):
        def __init__(self, error_message, context=None):
            """
            exception to catch errors caused by failure to connect to external services
            :param error_message: the message return from request
            :param context: other message suitable for troubleshooting errors
            """

            status_code = 500
            super().__init__(status_code, error_message, context=context)
