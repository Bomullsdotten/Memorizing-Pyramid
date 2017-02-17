import unittest

from pyramid import testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.conf = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        response = home(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'A link', response.body)

    def test_hi(self):
        from .views import hi

        request = testing.DummyRequest()
        respones = hi(request)

        self.assertEqual(respones.status_code, 200)
        self.assertIn(b"Another link", respones.body)

class FunctionalTestCase(unittest.TestCase):
    def setUp(self):
        from pack import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<body> A link', res.body)

    def test_hi(self):
        res = self.testapp.get('/hello', status=200)
        self.assertIn(b'<body> Another link', res.body)
if __name__ == '__main__':
    unittest.main()
