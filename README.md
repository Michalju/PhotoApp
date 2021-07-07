
# Welcome to the Photo Locations App (tailored Travel Bucket List) #



## The app fatures are as follows: ##              
### MVP 1 ###               
* The app allows the user to track countries and locaitons they want to visit and those they have visited.  The user is able to create and edit countries
* Each country can have one or more locaitons to visit 
* The user is able to create and delete entries for locations 
* The app allows the user to mark destinations as visited or still to see  

### Extension ###
* Have separate pages for locaitons visited and those still to visit
* Adds photos to the locaitons (currently on from py file)
*  Search for destination by continent, locaiton or country

### Other features  ###
* Home page displays 6 random locaitons
* Locations tiles shows random photo associated with the locaiton
* Sinlge location detailed page accessible from locaitons list

## Required packages: ## 
* PostgreSQL version 13.0
* Flask version 1.1.2
* psycopg2 version 2.8.6
* pillow 8.1.0
* requests 2.25.1

## Installation steps: ##
* createdb photo_locations
* psql -d photo_locations -f db/photo_locations.sql
* python3 console.py