import unittest
from http import HTTPStatus
from sk88_http_response.modules.http.objects.http_response import HTTPResponse
from sk88_http_response.tests.objects.user import User


class HTTPResponseTest(unittest.TestCase):

    def test_http_response_returns_success_below_400_code(self):
        user = User("bob", "jenkins")
        http_response = HTTPResponse(HTTPStatus.PERMANENT_REDIRECT, "", [user])

        response, code = http_response.get_response()

        self.assertEqual({
            "data": [user.get_http_dict()]
        }, response)
        self.assertEqual(HTTPStatus.PERMANENT_REDIRECT, code)

    def test_http_response_returns_error_above_400_code(self):
        message = "Error message"
        http_response = HTTPResponse(HTTPStatus.BAD_REQUEST, message)

        response, code = http_response.get_response()

        self.assertEqual({
            "message": message
        }, response)
        self.assertEqual(HTTPStatus.BAD_REQUEST, code)

    def test_http_response_returns_meta_data(self):
        user = User("bob", "jenkins")
        meta = {
            "test": 1
        }
        http_response = HTTPResponse(HTTPStatus.PERMANENT_REDIRECT, "", [user])
        http_response.set_meta(meta)

        response, code = http_response.get_response()

        self.assertEqual({
            "data": [user.get_http_dict()],
            "meta": meta
        }, response)
        self.assertEqual(HTTPStatus.PERMANENT_REDIRECT, code)
