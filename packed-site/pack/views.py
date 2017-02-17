from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home')
def home(request):
    return Response('<body> A link <a href="/hello">To somewhere</a></body>')

@view_config(route_name='hi')
def hi(request):
    return Response('<body> Another link <a href="/">To somewhere else</a></body>')