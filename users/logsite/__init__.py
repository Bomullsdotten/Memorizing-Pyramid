from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from .security import group_finder

def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    auth_policy = AuthTktAuthenticationPolicy(
        settings['user_site.secret'],
        callback=group_finder,
        hashalg='sha512'
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(auth_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('home', '/')
    config.add_route('page', '/page')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan('.views')

    return config.make_wsgi_app()