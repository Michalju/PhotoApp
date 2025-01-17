
# Welcome to the Photo Locations App  #



## The app fatures are as follows: ##              
### MVP 1 ###               
* The app allows the user to track countries and locaitons they want to visit and those they have visited.  The user is able to create and edit countries
* Each country can have one or more locaitons to visit 
* The user is able to create and delete entries for locations 
* The app allows the user to mark destinations as visited or still to see  
* Have separate pages for locaitons visited and those still to visit
* Adds photos to the locaitons (currently on from py file)
* Search for destination by continent, locaiton or country
* Home page displays 6 random locaitons
* Locations tiles shows random photo associated with the locaiton
* Single location detailed page accessible from locaitons list

### MVP 2 ###  
* Possible to upload photos to a location
* In progress: Get a weather forecast via API for a location based on GPS coordinates
* In progress: Ability to upload photos and to update GPS coordinates

### Future MVP 3 ###  
* Create React front-end interacting with Flask


### Future MVP 4 ###  
* Deploy the app to AWS or other cloud service.
* Add login for user/admin access.
* Make web accessible from external world.

## Required packages: ## 
* PostgreSQL version 13.0
* Flask version 2.9.1 (pip install Flask)
* psycopg2 version 2.8.6 (pip install psycopg2)
* pillow 8.3.1 (pip install Pillow)
* requests 2.25.1 (pip install requests)
* python dotenv 0.18.0 (pip install python-dotenv)

## Installation steps: ## Ensure user can login to DB
* createdb photo_locations
* psql -d photo_locations -f db/photo_locations.sql
* python console.py
