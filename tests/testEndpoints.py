import unittest

from hiveMod.flaskApp import app, readProjectVersion

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def testVersionEndpoint(self):
        expectedVersion = str(readProjectVersion())
        response = self.app.get('/version')
        self.assertEqual(response.status_code, 200)
        self.assertIn(expectedVersion, response.get_data(as_text=True))

    def testTemperatureEndpoint(self):
        response = self.app.get('/temperature')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p>Values measured', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()