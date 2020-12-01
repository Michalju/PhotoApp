import unittest
from models.continent import Continent
from models.country import Country
from models.location import Location

class TestLocation(unittest.TestCase):
    
    # This is to setup countries for test
    def setUp(self):
        self.europe = Continent("Europe", 2)
        self.scotland = Country("Scotland", self.europe, 1)
        self.iceland = Country("Iceland", self.europe, 3)

        self.glencoe = Location("Glencoe", "This is stunning location, i need to see it", False, self.scotland, 1)
        self.godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, self.iceland, 2)
        self.no_id = Location("No id", "locaiton without id", True,self.scotland)

    # Verifies location name has been setup correctly
    def test_location_name(self):
        self.assertEqual(self.glencoe.name, "Glencoe")
        self.assertEqual(self.godafoss.name, "Godafoss")
        
    # Verifies location description has been setup correctly
    def test_location_description(self):
        self.assertEqual(self.glencoe.description, "This is stunning location, i need to see it")
        self.assertEqual(self.godafoss.description, "The most amazing waterfall i have ever seen")

    # Verifies location visited has been setup correctly
    def test_location_visited(self):
        self.assertEqual(self.glencoe.visited, False)
        self.assertEqual(self.godafoss.visited, True)

    # Verifies location country has been setup correctly
    def test_location_country(self):
        self.assertEqual(self.glencoe.country.name, "Scotland")
        self.assertEqual(self.godafoss.country.name, "Iceland")

    # Verifies location id has been setup correctly
    def test_location_id(self):
        self.assertEqual(self.glencoe.id, 1)
        self.assertEqual(self.godafoss.id, 2)
        self.assertEqual(self.no_id.id, None)

    # Verifies location _random_photo has been setup correctly
    def test_location_random_photo(self):
        self.assertEqual(self.glencoe._random_photo, None)
        self.assertEqual(self.godafoss._random_photo, None)