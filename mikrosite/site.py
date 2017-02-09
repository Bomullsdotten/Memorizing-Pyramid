from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print("incoming request")
    return Response('<body><h1>Hi, I\'m practicing</h1></body>')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hi', '/')
    config.add_view(hello_world, route_name='hi')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app)
    server.serve_forever()
