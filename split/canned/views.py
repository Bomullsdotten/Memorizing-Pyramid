from pyramid.view import view_config


@view_config(route_name='home', renderer='base.jinja2')
def home(request):
    return dict(
        title='Home',
        text='I am home'
    )


@view_config(route_name='screen', renderer='base.jinja2')
def screen(request):
    return dict(
        title='Screen',
        text='Hello my dear screen'
    )


