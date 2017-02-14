from wsgiref.simple_server import make_server

from pyramid.response import Response
from pyramid.config import Configurator

def hi(request):
    print("so far so good")
    return Response("<body><h1>Testing testing</h1></body>")


if __name__ == "__main__":
    conf = Configurator()
    conf.add_route('home', '/')
    conf.add_view(hi, route_name='home')
    app = conf.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app)
    server.serve_forever()
