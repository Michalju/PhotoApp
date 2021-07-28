import unittest
from models.continent import Continent
from models.country import Country
from models.location import Location
from models.file import File
from werkzeug.datastructures import FileStorage
import os
#os.path.isfile('./final_data.csv')
class TestFile(unittest.TestCase):
    
    # This is to setup countries for test
    def setUp(self):
        self.europe = Continent("Europe", 2)
        self.scotland = Country("Scotland", self.europe, 1)
        self.iceland = Country("Iceland", self.europe, 3)

        self.glencoe = Location("Glencoe", "This is stunning location, i need to see it", False, self.scotland, 1)
        self.godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, self.iceland, 2)
        self.no_id = Location("No id", "locaiton without id", True,self.scotland)
        self.test_file = None
        with open("tests/Glencoe_001.jpg") as fp:
             self.test_file = FileStorage(fp)
        self.photo_01 = File(self.glencoe,self.test_file)
        self.photo_02 = File(self.godafoss,self.test_file)

    # Verifies location name has been setup correctly
    def test_file_location_name(self):
         self.assertEqual(self.photo_01._location_name, "Glencoe")

    # Verifies storage path is correct
    def test_storage_path(self):
        self.assertEqual(self.photo_01._storage_path ,"static/photos")


    # Verifies file name was set and saved correctly
    def test_save(self):   
        self.photo_01._storage_path = "tests"
        self.photo_01.get_filename()
        self.photo_02._storage_path = "tests"
        self.photo_02.get_filename()

        self.assertEqual(self.photo_01._file_name ,"Glencoe_004")
        self.assertEqual(self.photo_02._file_name ,"Godafoss_001")

    # Verifies allwoed extension are configured correctly
    #def test_allowed_extension(self): 
        # self._allowed_extensions = ['.jpg', '.png', '.gif']
   
        
        # file = None
        # with open('tests/test.jpg', 'rb') as fp:
        #     file = FileStorage(fp)
        # self.godafoss_photo_03.file_storage=file