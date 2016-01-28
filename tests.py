import unittest
import app

class GeolocatorTest(unittest.TestCase):
    def test_geolocation(self):
        print app.geolocate_address_string("1168 Folsom St. San Francisco CA 94107")

if __name__ == '__main__':
    unittest.main()