import unittest

from pyramid import testing

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        #some more here...

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from canned.views import home
        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual('I am home', response['text'])

    def test_screen(self):
        from canned.views import screen
        request = testing.DummyRequest()
        response = screen(request)

        self.assertEqual('Screen', response['title'])



from webtest import TestApp

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from canned import main
        app = main({})
        self.app = TestApp(app)
        #think this is right


    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'I am home', response.body)

    def test_screen(self):
        response = self.app.get('/screen')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello my dear screen', response.body)



if __name__ == '__main__':
    unittest.main()
