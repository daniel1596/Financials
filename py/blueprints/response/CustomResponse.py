from flask import make_response
from flask.wrappers import Response


class CustomResponse:
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