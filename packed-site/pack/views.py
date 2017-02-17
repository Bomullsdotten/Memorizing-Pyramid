from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(renderer='home.jinja2')
class PageViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return dict(
            name='Home View'
        )

    @view_config(route_name='hi')
    def hi(self):
        return dict(
            name='Hello View'
        )
