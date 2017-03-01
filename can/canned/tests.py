import unittest
from pyramid import testing

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        #hmm

    def tearDown(self):
        testing.tearDown()



    def test_home(self):
        from canned.views import home
        request = testing.DummyRequest()
        response = home(request)

        self.assertEqual('Home alone?', response['title'])

import webtest
class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from canned import main
        app = main({})
        self.app = webtest.TestApp(app)


    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No, I have my dog', response.body)

    def test_json(self):
        response = self.app.get('/.json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"title": "Home alone?", "text": "No, I have my dog, it\'s called Json"}', response.body)


if __name__ == '__main__':
    unittest.main()
