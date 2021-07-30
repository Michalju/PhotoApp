import os
from werkzeug.utils import secure_filename
class File:
    def __init__(self, location, file, storage_path):
        self._location_name= location.name
        self.file = file
        self.storage_path = storage_path
        self._file_name = ""
        self._file_name_with_extension = ""
        self._file_extension = os.path.splitext(secure_filename((self.file.filename)))[1]
        self.get_filename()
        self.save()
  


    # goes through the folder and tries to find out free id for new photo to be save i.e. if files
    # are location_001, location_002 then free i.d. is 003
    def get_filename(self):
        file_list = []
        for file in os.listdir(self.storage_path):
            if file.startswith(self._location_name):
                dot_position = file.find(".")
                file_list.append(int(file[dot_position-3:dot_position]))
        if file_list:
            self._file_name =self._location_name + "_" + f'{(max(file_list)+1):03d}'
        else:
            self._file_name =self._location_name + "_001"

    def save(self):
        self._file_name_with_extension = self._file_name + self._file_extension
        self.file.save(os.path.join(self.storage_path, self._file_name_with_extension))        