from flask import make_response
from flask.wrappers import Response


class CustomResponse:
    """
    Wanted to have a basic response class for some custom data that leveraged Flask's built-in methods.
    Subject to change, but for now it's nice to have.
    """

    @classmethod
    def success(cls, message: str) -> Response:
        return make_response({
            'message': message,
            'is_successful': True
        })

    @classmethod
    def error(cls, message: str) -> Response:
        return make_response({
            'message': message,
            'is_successful': False
        })