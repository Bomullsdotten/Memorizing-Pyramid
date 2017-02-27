import unittest

from pyramid import testing


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home
        request = testing.DummyRequest()
        response = home(request=request)

        self.assertEqual('Home', response['title'])

    def test_hello(self):
        from .views import hello
        request = testing.DummyRequest()
        response = hello(request)

        self.assertEqual('Hello', response['title'])


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from split_site import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        response = self.testapp.get('/', status=200)
        self.assertIn(b'Jay', response.body)

    def test_hello(self):
        response = self.testapp.get('/hello', status=200)
        self.assertIn(b'Hello Screen', response.body)