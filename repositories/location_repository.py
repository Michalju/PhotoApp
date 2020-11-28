# Import run_sql function
from db.run_sql import run_sql

# Import location class
from models.location import Location
import repositories.country_repository as country_repository

# create save function   
def save(location):
    # create sql query without values
    sql = "INSERT INTO locations (name, description, visited, country_id) VALUES (%s, %s, %s, %s) RETURNING id"
    # create list with values required by sql query
    values = [location.name, location.description, location.visited, location.country.id]
    # execute sql query
    results = run_sql(sql, values)
    # obtain id from the query result and put it into the class
    id = results[0]['id']
    location.id = id

# create select all function     
def select_all():
     # set return variable as empty list
    locations = []
    # create sql query without values
    sql = "SELECT * FROM locations"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of locations objects
    for result in results:        
        location = Location(result["name"], result["description"], result["visited"], country_repository.select(result['country_id']),result["id"]) 
        locations.append(location)
    # return the result 
    return locations

# create select by id function    
def select(id):
    # create sql query without values
    sql = "SELECT * FROM locations WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    result = run_sql(sql, values)[0]
    # convert return which is a single element list of dictionaries into a continent object
    location = Location(result["name"], result["description"], result["visited"], country_repository.select(result['country_id']),result["id"])
    # return the result 
    return location

# create delete all function    
def delete_all():
     # create sql query
    sql = "DELETE FROM locations"
    # execute sql query
    run_sql(sql)

# create delete by id function    
def delete(id):
    # create sql query without values
    sql = "DELETE FROM locations WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    run_sql(sql, values)
    
# create update function    
def update(location):
    # create sql query without values
    sql = "UPDATE locations SET (name, description, visited, country_id) = (%s, %s, %s, %s) WHERE id = %s"
    # create list with values required by sql query
    values = [location.name, location.description, location.visited, location.country.id, location.id]
    # execute sql query
    run_sql(sql, values)

# create select all visited locations function     
def visited():
     # set return variable as empty list
    locations = []
    # create sql query without values
    sql = "SELECT * FROM locations WHERE visited = True"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of locations objects
    for result in results:        
        location = Location(result["name"], result["description"], result["visited"], country_repository.select(result['country_id']),result["id"]) 
        locations.append(location)
    # return the result 
    return locations

# create select all to be_visited locations function     
def to_be_visited():
     # set return variable as empty list
    locations = []
    # create sql query without values
    sql = "SELECT * FROM locations WHERE visited = False"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of locations objects
    for result in results:        
        location = Location(result["name"], result["description"], result["visited"], country_repository.select(result['country_id']),result["id"]) 
        locations.append(location)
    # return the result 
    return locations