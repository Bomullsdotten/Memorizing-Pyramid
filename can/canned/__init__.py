from pyramid.config import Configurator
from pyramid.response import Response


def hi(request):
    print("let's see")
    return Response(b"<body><h1> Cant wait to use templates</h1></body>")


def main(global_config, **settings):
    conf = Configurator(settings=settings)
    conf.add_route('hi', '/')
    conf.add_view(hi, route_name='hi')

    return conf.make_wsgi_app()