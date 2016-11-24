import unittest

import falcon.testing


class HelloResourceTest(falcon.testing.TestCase):
    def test_get(self):
        """GET /hello works."""
        pass


if __name__ == '__main__':
    unittest.main()
