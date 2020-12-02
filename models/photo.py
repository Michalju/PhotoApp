from PIL import Image
import PIL.ExifTags

class Photo:
    def __init__(self, filename, mine, location, id = None):
        self.filename = filename
        self.mine=mine
        self.location=location
        self.id=id
        self._file_location = "static/photos/"+ self.filename
        self.exif_details =  {
            "camera_make": "",    # Exif id 271 (0x010f)
            "camera_model": "",   # Exif id 272 (0x0110)
            "lens_make": "",      # Exif id 42035 (0xa433)
            "lens_model": "",     # Exif id 42036 (0xa434)
            "aperture": "",       # Exif id 37378 (0x9202)
            "shutter_speed": "",  # Exif id 37377 (0x9201)
            "iso": ""             # Exif id 34855 (0x8827)
        }
        self.gps_location = {
            "latitude":"",  
            "longitude":""}
        self.get_photo_info()  
        self.get_coordinates()
    # The purpose of this function is to:
    # - Extract GPS coordinates from exif
    # Function returns None if no GPS coordinates
    def get_coordinates(self):
        image = Image.open(self._file_location)
        exif_data_PIL = image._getexif()
        image.close()
        # checks if exif and GPS data (id 34853) data exists
        if exif_data_PIL and 34853 in exif_data_PIL:
        # Converting GPS from degrees, minutes, and seconds DMS to Decimal degrees (DD)
        # see https://en.wikipedia.org/wiki/Decimal_degrees for more info
        # For info about GPS tags within exif file refer to https://exiftool.org/TagNames/GPS.html
            Latitude = exif_data_PIL[34853][2][0] + exif_data_PIL[34853][2][1]/60.0 + exif_data_PIL[34853][2][2]/3600.0
            Longitude = exif_data_PIL[34853][4][0] + exif_data_PIL[34853][4][1]/60.0 + exif_data_PIL[34853][4][2]/3600.0
            if exif_data_PIL[34853][1] == 'S':
                Latitude *= -1
            if exif_data_PIL[34853][3] == 'W':
                Longitude *= -1
            self.gps_location = {
                "latitude":Latitude, "longitude":Longitude}

    def get_photo_info(self):


        image = Image.open(self._file_location)
        exif_data_PIL = image._getexif()
        image.close()
        if exif_data_PIL:
            if 271 in exif_data_PIL:
                self.exif_details["camera_make"] = exif_data_PIL[271]
            if 272 in exif_data_PIL:
                self.exif_details["camera_model"] = exif_data_PIL[272]
            if 42035 in exif_data_PIL:
                self.exif_details["lens_make"] = exif_data_PIL[42035]
            if 42036 in exif_data_PIL:
                self.exif_details["lens_model"] = exif_data_PIL[42036]
            if 37378 in exif_data_PIL:
                self.exif_details["aperture"] = round(pow(2,exif_data_PIL[37378]/2),1)
            if 37377 in exif_data_PIL:
                self.exif_details["shutter_speed"] = round(pow(2,exif_data_PIL[37377]),1)
            if 34855 in exif_data_PIL:
                self.exif_details["iso"] = exif_data_PIL[34855]