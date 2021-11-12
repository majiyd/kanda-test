import json
import falcon
from marshmallow import schema, ValidationError
from marshmallow.utils import pprint

from schemas.signup import SignupSchema


class SignupResource:
    def on_get(self, req, resp):
        """Handles get Request for sign up"""
        quote = {
            'author': "hi"
        }

        resp.body = json.dumps(quote)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        """handles post request"""

        try:
            if req.content_length in (None, 0):
                return

            body = json.loads(req.bounded_stream.read())

            SignupSchema().load(body)

            resp.body = json.dumps({})
            resp.status = falcon.HTTP_201

        except ValidationError as err:
            resp.body = json.dumps({
                "error": "Bad request",
                "field_errors": err.messages,
                "data": body
            })
            resp.status = falcon.HTTP_400
