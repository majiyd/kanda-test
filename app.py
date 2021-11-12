from wsgiref.simple_server import make_server
import falcon

from signup import SignupResource


def create():
    app = falcon.App()
    signupHandler = SignupResource()
    app.add_route('/', signupHandler)
    return app


# initialize app
app = application = create()
