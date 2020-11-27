import unittest
from models.country import Country
from models.continent import Continent

class TestCountry(unittest.TestCase):
    
    # This is to setup countries for test
    def setUp(self):
        self.asia = Continent("Asia", 1)
        self.europe = Continent("Europe", 2)

        self.scotland = Country("Scotland", self.europe, 1)
        self.singapore = Country("Singapore", self.asia, 2)
        self.iceland = Country("Iceland", self.europe, 3)
        self.no_id = Country("No Id", self.europe)

    # Verifies country name has been setup correctly
    def test_country_name(self):
        self.assertEqual(self.scotland.name, "Scotland")
        self.assertEqual(self.singapore.name, "Singapore")
        self.assertEqual(self.iceland.name, "Iceland")

    # Verifies continent has been setup correctly
    def test_country_continent_name(self):
        self.assertEqual(self.scotland.continent.name, "Europe")
        self.assertEqual(self.singapore.continent.name, "Asia")
        self.assertEqual(self.iceland.continent.name, "Europe")

    # Verifies country id has been setup correctly
    def test_country_id(self):
        self.assertEqual(self.scotland.id, 1)
        self.assertEqual(self.singapore.id, 2)
        self.assertEqual(self.iceland.id, 3)
        self.assertEqual(self.no_id.id, None)