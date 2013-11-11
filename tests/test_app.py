import unittest

import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.headers["Location"], "http://www.meetup.com/PyLadiesDublin/")

if __name__ == '__main__':
    unittest.main()
