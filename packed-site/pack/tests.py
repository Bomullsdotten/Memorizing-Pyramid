import unittest

from pyramid import testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.conf = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import PageViews

        request = testing.DummyRequest()
        instance = PageViews(request)
        response = instance.home()

        self.assertEqual('Home View', response['name'])

    def test_hi(self):
        from .views import PageViews

        request = testing.DummyRequest()
        instance = PageViews(request)
        response = instance.hi()

        self.assertEqual('Hello View', response['name'])


class FunctionalTestCase(unittest.TestCase):
    def setUp(self):
        from pack import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home View', res.body)

    def test_hi(self):
        res = self.testapp.get('/hello', status=200)
        self.assertIn(b'<h1>Hi Hello View', res.body)

if __name__ == '__main__':
    unittest.main()
