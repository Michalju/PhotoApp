import sys

class Photo:
    def __init__(self, image, mine, location, id = None):
        self.image = self.readImage(image)
        self.mine=mine
        self.location=location
        self.id=id

    def readImage(self, filename):
        fin = None
        try:
            fin = open(filename, "rb")
            img = fin.read()
            return img

        except IOError as e:

            print(f'Error {e.args[0]}, {e.args[1]}')
            sys.exit(1)

        finally:

            if fin:
                fin.close()