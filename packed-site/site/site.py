from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response

def a_function(request):
    print('guess i\'l make a microsite for now')
    return Response('<body><h1> something different<h1> <body>')

if __name__ == "__main__":
    config = Configurator()
    config.add_route('something', '/')
    config.add_view(a_function, route_name='something')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app)
    server.serve_forever()