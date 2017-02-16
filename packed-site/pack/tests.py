import unittest

from pyramid import testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.conf = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from pack import hello_world
        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)


class FunctionalTestCase(unittest.TestCase):
    def setUp(self):
        from pack import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_hello_world(self):

        response = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>testing</h1>', response.body)


if __name__ == '__main__':
    unittest.main()
