from pyramid.view import view_config


@view_config(route_name='json', renderer='json')
@view_config(route_name='home', renderer='base.jinja2')
def home(request):
    return dict(
        title='Home alone?',
        text='No, I have my dog, it\'s called Json',
    )

