import unittest
from models.continent import Continent
from models.country import Country
from models.location import Location
from models.photo import Photo

class TestPhoto(unittest.TestCase):
        
    # This is to setup countries for test
    def setUp(self):
        self.europe = Continent("Europe", 2)
        self.scotland = Country("Scotland", self.europe, 1)
        self.iceland = Country("Iceland", self.europe, 3)

        self.glencoe = Location("Glencoe", "This is stunning location, i need to see it", False, self.scotland, 1)
        self.godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, self.iceland, 2)

        self.glencoe_photo = Photo("devils_pulpit.jpg", True, self.glencoe, 1)
        self.godafoss_photo_01 = Photo("marina_sands01.jpg", True, self.godafoss, 2)
        self.godafoss_photo_02 = Photo("marina_sands01.jpg", True, self.godafoss)        


    # Verifies photo filename has been setup correctly
    def test_photo_filename(self):
        self.assertEqual(self.glencoe_photo.filename,"devils_pulpit.jpg")
        self.assertEqual(self.godafoss_photo_01.filename, "marina_sands01.jpg")



    # Verifies photo mine has been setup correctly
    def test_photo_mine(self):
        self.assertEqual(self.glencoe_photo.mine, True)
        self.assertEqual(self.godafoss_photo_01.mine, False)
        
    # Verifies photo location has been setup correctly
    def test_photo_mine(self):
        self.assertEqual(self.glencoe_photo.location.id, 1)
        self.assertEqual(self.godafoss_photo_01.location.id, 2)

    # Verifies photo id has been setup correctly
    def test_photo_id(self):
        self.assertEqual(self.glencoe_photo.id, 1)
        self.assertEqual(self.godafoss_photo_01.id, 2)
        self.assertEqual(self.godafoss_photo_02.id, None)