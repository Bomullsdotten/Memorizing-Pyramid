import logging

log = logging.getLogger(__name__)

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget

from pyramid.view import view_config
from pyramid.view import view_defaults

from .security import USERS
from .security import check_password


@view_defaults(renderer='base.jinja2')
class HomeViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='home')
    def home(self):
        log.debug('value of self.logged_in is ' + str(self.logged_in))
        return dict(
            title='Home view'
        )

    @view_config(route_name='page', permission='edit')
    def page(self):
        log.debug('value of self.logged_in is ' + str(self.logged_in))
        return dict(
            title='¨Page view'
        )

    @view_config(route_name='login', renderer='login.jinja2')
    def login(self):
        log.debug('Inside Login view')
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            log.debug('form.submitted was a success')
            login = request.params['login']
            password = request.params['password']
            if check_password(password, USERS.get(login)):
                headers = remember(request, login)
                logging.debug('Managed to login')
                return HTTPFound(location=came_from, headers=headers)
            message = 'Failed Login'
        log.debug('Return error messages')
        return dict(
            title='Login',
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            login=login,
            password=password
        )


    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url,
                         headers=headers)
