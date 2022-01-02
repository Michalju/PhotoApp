class Location:
    def __init__(self, name, description, visited, latitude, longitude, coutry, id = None):
        self.name = name
        self.description=description
        self.visited=visited
        self.latitude=latitude
        self.longitude=longitude
        self.country=coutry
        self.id=id
        self._random_photo = None