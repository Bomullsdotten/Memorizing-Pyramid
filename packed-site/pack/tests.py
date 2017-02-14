import unittest

from pyramid import testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.conf = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_something(self):
        from pack import hello_world
        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
