from pyramid.config import Configurator

def main(globals, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('json', '/.json')
    config.scan('.views')
    return config.make_wsgi_app()