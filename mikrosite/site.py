from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator


def hello(request):
    print('last time i think')
    return Response(b"<body><h1>Hello pc screen</h1></body>")

if __name__ == '__main__':
    conf = Configurator()
    conf.add_route('hello', '/')
    conf.add_view(hello, route_name='hello')
    app = conf.make_wsgi_app()
    server = make_server('0.0.0.0', 6500, app)
    server.serve_forever()
