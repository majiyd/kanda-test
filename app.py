import falcon
from signup import SignUp

app = application = falcon.App()

app.add_route('/', SignUp())
