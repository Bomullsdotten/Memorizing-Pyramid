import unittest
from pyramid import testing


class TestSuite(unittest.TestCase):
    def test_hi(self):
        from can.canned import hi
        req = testing.DummyRequest()
        response = hi(request=req)
        self.assertEqual(response.status_code, 200)
        