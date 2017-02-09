from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response


def a_function(request):
    print('Guess i remembered most things')
    return Response("<body><h1> Second attempt <h1><body>")


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hi', '/')
    config.add_view(a_function, route_name='hi')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app)
    server.serve_forever()

