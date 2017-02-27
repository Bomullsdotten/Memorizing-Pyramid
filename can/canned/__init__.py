from pyramid.response import Response
from pyramid.config import Configurator


def hi(request):
    return Response("<body><p1>Forgot Something</p1></body>")


def main(app_globals, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hi, route_name='hello')

    return config.make_wsgi_app()
