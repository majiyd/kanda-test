import json
import falcon


class SignUp:
    def on_get(self, req, resp):
        """Handles get Request for sign up"""
        quote = {
            'author': "hi"
        }

        resp.body = json.dumps(quote)
        resp.status = falcon.HTTP_200
