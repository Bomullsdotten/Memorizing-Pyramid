from pyramid.view import view_config


@view_config(route_name='home', renderer='base.jinja2')
def home(request):
    return dict(
        title='Home',
        text='Jay'
    )


@view_config(route_name='hello', renderer='base.jinja2')
def hello(request):
    return dict(
        title='Hello',
        text='Hello Screen'
    )
