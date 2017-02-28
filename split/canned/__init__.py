from pyramid.config import Configurator

def main(global_values, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('screen', '/screen')
    config.scan('.views')
    return config.make_wsgi_app()
