from wsgiref.simple_server import make_server
import falcon

from signup import SignupResource

app = falcon.App()

signupHandler = SignupResource()
app.add_route('/', signupHandler)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
