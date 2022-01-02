import unittest
from models.continent import Continent
from models.country import Country
from models.location import Location
from models.file import File
from werkzeug.datastructures import FileStorage
import os
class TestFile(unittest.TestCase):    
    # This is to setup countries for test
    def setUp(self):
        self.europe = Continent("Europe", 2)
        self.scotland = Country("Scotland", self.europe, 1)
        self.iceland = Country("Iceland", self.europe, 3)

        self.glencoe = Location("Glencoe", "This is stunning location, i need to see it", False, "56.6825599", "-5.1022713", self.scotland, 1)
        self.godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, "", "", self.iceland, 2)
        self.no_id = Location("No id", "locaiton without id", True, "", "",self.scotland)
        self.test_file = None

    # Verifies location name has been setup correctly
    def test_file_location_name(self):
        with open("tests/Glencoe_001.jpg", 'rb') as fp:
            self.test_file = FileStorage(fp)
            self.photo_01 = File(self.glencoe,self.test_file,"tests")

        self.assertEqual(self.photo_01._location_name, "Glencoe")
        os.remove('tests/Glencoe_004.jpg')

    # Verifies storage path is correct
    def test_storage_path(self):
        with open("tests/Glencoe_001.jpg", 'rb') as fp:
            self.test_file = FileStorage(fp)
            self.photo_01 = File(self.glencoe,self.test_file,"tests")

        self.assertEqual(self.photo_01.storage_path ,"tests")
        os.remove('tests/Glencoe_004.jpg')


    # Verifies file name was set and saved correctly
    def test_save(self):   
        # with open("tests/Glencoe_001.jpg", 'rb') as fp:
        with open("tests/Glencoe_001.jpg", 'rb') as fp:
            self.test_file = FileStorage(fp)
            self.photo_01 = File(self.glencoe,self.test_file,"tests")
            self.test_file = FileStorage(fp)
            self.photo_02 = File(self.godafoss,self.test_file,"tests")

        self.assertEqual(self.photo_01._file_name ,"Glencoe_004")
        self.assertEqual(self.photo_02._file_name ,"Godafoss_001")
   
        self.assertTrue(os.path.isfile('tests/Godafoss_001.jpg'))   
        self.assertTrue(os.path.isfile('tests/Glencoe_004.jpg'))
        os.remove('tests/Godafoss_001.jpg')
        os.remove('tests/Glencoe_004.jpg')