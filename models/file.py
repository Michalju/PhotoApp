import os
class File:
    def __init__(self, location, file):
        self._location_name= location.name
        self.file = file
        self._storage_path = "static/photos"
        self._file_name = ""
        self._allowed_extensions = ['.jpg', '.png', '.gif']


    # goes through the folder and tries to find out free id for new photo to be save i.e. if files
    # are location_001, location_002 then free i.d. is 003
    def get_filename(self):
        file_list = []
        for file in os.listdir(self._storage_path):
            if file.startswith(self._location_name):
                dot_position = file.find(".")
                file_list.append(int(file[dot_position-3:dot_position]))
        if file_list:
            self._file_name =self._location_name + "_" + f'{(max(file_list)+1):03d}'
        else:
            self._file_name =self._location_name + "_001"

        