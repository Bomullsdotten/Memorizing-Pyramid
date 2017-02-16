
from pyramid.config import Configurator
from pyramid.response import Response


def hello(request):
    pass

def main(app_construct,**settings):
    config = Configurator(settings=settings)
    config.add_route('hi', '/')
    config.add_view(hello, route_name='hi')

    return config.make_wsgi_app()