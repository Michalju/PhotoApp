import pdb

from models.continent import Continent
from models.country import Country
from models.location import Location

import repositories.continent_repository as continent_repository
import repositories.country_repository as country_repository
import repositories.location_repository as location_repository

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

# populates continent table
glencoe = Location("Glencoe", "This is stunning location, i need to see it", False, scotland)
glenfinnan = Location("Glenfinnan", "Awsome Harry Potter bridge", True, scotland)
godafoss = Location("Godafoss", "The most amazing waterfall i have ever seen", True, iceland)
bluelagoon = Location("Blue Lagoon", "Amazing thermal pools", False, iceland)
clar_quay = Location("Clark Quay", "Good to stay", True, singapore)
sentosa = Location("Sentosa", "Some entertainment there", True, singapore)
marin_sands_bay = Location("Marina Sands Bay", "Nice night photography", True, singapore)
alps = Location("Alps", "Excellent glacier photo oportunity", False, austria) 
namibia_dunes = Location("Namibia Dunes", "Excellent dunes photo oportunity", False, namibia) 

location_repository.save(glencoe)
location_repository.save(glenfinnan)
location_repository.save(godafoss)
location_repository.save(bluelagoon)

location_repository.save(clar_quay)
location_repository.save(sentosa)
location_repository.save(marin_sands_bay)
location_repository.save(alps)
location_repository.save(namibia_dunes)


pdb.set_trace()