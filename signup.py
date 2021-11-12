import json
import falcon
from marshmallow import schema, ValidationError
from marshmallow.utils import pprint

from schemas.signup import SignupSchema


class SignupResource:
    def on_post(self, req, resp):
        """handles sign up request"""

        try:
            # ensure body is not empty
            if req.content_length in (None, 0):
                SignupSchema().load({})

            body = json.loads(req.bounded_stream.read())

            # validate data
            SignupSchema().load(body)

            resp.body = json.dumps({})
            resp.status = falcon.HTTP_201

        except ValidationError as err:
            resp.body = json.dumps({
                "error": "Bad request",
                "field_errors": err.messages,
            })
            resp.status = falcon.HTTP_400
