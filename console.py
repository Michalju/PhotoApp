import pdb

from models.continent import Continent
import repositories.continent_repository as continent_repository

continent_repository.delete_all()

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

pdb.set_trace()