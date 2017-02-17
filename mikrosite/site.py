from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response


def hi(request):
    print("so far so good")
    return Response("<body><h1>Hello Screen</h1></body>")


if __name__ == '__main__':
    conf = Configurator()
    conf.add_route('hello', '/')
    conf.add_view(hi, route_name='hello')
    app = conf.make_wsgi_app()

    server = make_server('0.0.0.0', 6500, app=app)
    server.serve_forever()