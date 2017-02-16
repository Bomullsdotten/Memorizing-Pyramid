from wsgiref.simple_server import make_server

from pyramid.response import Response
from pyramid.config import Configurator

def hi(request):
    print("getting the hands of it now.")
    return Response("<body><h1>Should i change things up?</h1></body>")


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hi', '/')
    config.add_view(hi, route_name='hi')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app=app)
    server.serve_forever()