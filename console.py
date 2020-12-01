import pdb
import sys

from models.continent import Continent
from models.country import Country
from models.location import Location
from models.photo import Photo

import repositories.continent_repository as continent_repository
import repositories.country_repository as country_repository
import repositories.location_repository as location_repository
import repositories.photo_repository as photo_repository

# clear tables
location_repository.delete_all()
country_repository.delete_all()
continent_repository.delete_all()

# populates continent table
africa = Continent("Africa")
continent_repository.save(africa)

asia = Continent("Asia")
continent_repository.save(asia)

europe = Continent("Europe")
continent_repository.save(europe)

north_america = Continent("North America")
continent_repository.save(north_america)

south_america = Continent("South America")
continent_repository.save(south_america)

antarctica = Continent("Antarctica")
continent_repository.save(antarctica)

australia = Continent("Australia")
continent_repository.save(australia)

# populates contry table
scotland = Country("Scotland", europe)
country_repository.save(scotland)

singapore = Country("Singapore", asia)
country_repository.save(singapore)

iceland = Country("Iceland", europe)
country_repository.save(iceland)

austria = Country("Austria", europe)
country_repository.save(austria)

namibia = Country("Namibia", africa)
country_repository.save(namibia)

# populates locations table with visited places
glencoe = Location("Glencoe", "This is stunning location...", True, scotland)
glenfinnan = Location("Glenfinnan", "Awsome Harry Potter bridge", True, scotland)
godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, iceland)
lava_field = Location("Lava field", "Size fo this fields shows an impact of a vulcanic erruption.", True, iceland)
clark_quay = Location("Clark Quay", "Good to stay", True, singapore)
marina_sands_bay = Location("Marina Sands Bay", "Nice night photography", True, singapore)
marina_bay_gardens = Location("Marina Bay Gardens", "Incredible garens with stunning artificial trees", True, singapore)
devils_pulpit = Location("Devils Pulpit", "Awesome colours", True, scotland)

location_repository.save(glencoe)
location_repository.save(glenfinnan)
location_repository.save(godafoss)
location_repository.save(lava_field)
location_repository.save(clark_quay)
location_repository.save(marina_sands_bay)
location_repository.save(marina_bay_gardens)
location_repository.save(devils_pulpit)

# populates locations table with to be visited places
bluelagoon = Location("Blue Lagoon", "Amazing thermal pools", False, iceland)
sentosa = Location("Sentosa", "Some entertainment there", False, singapore)
alps = Location("Alps", "Excellent glacier photo oportunity", False, austria) 
namibia_dunes = Location("Namibia Dunes", "Excellent dunes photo oportunity", False, namibia) 

location_repository.save(bluelagoon)
location_repository.save(sentosa)
location_repository.save(alps)
location_repository.save(namibia_dunes)

photo_repository.save(Photo("Clark01.jpg", True, clark_quay))
photo_repository.save(Photo("Godafoss02.jpg", True, godafoss))
photo_repository.save(Photo("MarinaGardens01.jpg", True, marina_bay_gardens))
photo_repository.save(Photo("Glencoe01.jpg", True, glencoe))
photo_repository.save(Photo("Lava field.jpg", True, lava_field))
photo_repository.save(Photo("MarinaGardens02.jpg", True, marina_bay_gardens))
photo_repository.save(Photo("Glencoe02.jpg", True, glencoe))
photo_repository.save(Photo("Marina01.jpg", True, marina_sands_bay))
photo_repository.save(Photo("devils_pulpit.jpg", True, devils_pulpit))
photo_repository.save(Photo("Glencoe03.jpg", True, glencoe))
photo_repository.save(Photo("Marina02.jpg", True, marina_sands_bay))
photo_repository.save(Photo("marina_sands01.jpg", True, marina_sands_bay))
photo_repository.save(Photo("Glenfinnan01.jpg", True, glenfinnan))
photo_repository.save(Photo("Marina03.jpg", True, marina_sands_bay))
photo_repository.save(Photo("Godafoss01.jpg", True, godafoss))
photo_repository.save(Photo("Marina04.jpg", True, marina_sands_bay))

pdb.set_trace()