import unittest
from models.continent import Continent

class TestContinent(unittest.TestCase):
    
    # This is to setup continents for test
    def setUp(self):
        self.africa = Continent("Africa",1)
        self.asia = Continent("Asia",2)
        self.europe = Continent("Europe",3)
        self.north_america = Continent("North America", 4)
        self.south_america = Continent("South America", 5)
        self.antarctica = Continent("Antarctica", 6)
        self.australia = Continent("Australia", 7)
        self.no_id = Continent("No Id")
    
    # Verifies continent name has been setup correctly
    def test_continent_name(self):
        self.assertEqual(self.africa.name, "Africa")
        self.assertEqual(self.asia.name, "Asia")
        self.assertEqual(self.europe.name, "Europe")
        self.assertEqual(self.north_america.name, "North America")
        self.assertEqual(self.south_america.name, "South America")
        self.assertEqual(self.antarctica.name, "Antarctica")
        self.assertEqual(self.australia.name, "Australia")

    # Verifies continent id has been setup correctly
    def test_continent_id(self):  
        self.assertEqual(self.africa.id, 1)
        self.assertEqual(self.asia.id, 2)
        self.assertEqual(self.europe.id, 3)
        self.assertEqual(self.north_america.id, 4)
        self.assertEqual(self.south_america.id, 5)
        self.assertEqual(self.antarctica.id, 6)
        self.assertEqual(self.australia.id, 7)
        self.assertEqual(self.no_id.id, None)