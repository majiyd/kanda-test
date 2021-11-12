import json
import falcon
from marshmallow import schema, ValidationError

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
            SignupSchema(strict=True).load({})

            resp.body = json.dumps({"5": "56"})
            resp.status = falcon.HTTP_201

        except ValidationError as err:
            resp.body = json.dumps(err.messages)
            resp.status = falcon.HTTP_400
