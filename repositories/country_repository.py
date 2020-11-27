# Import run_sql function
from db.run_sql import run_sql

# Import country class
from models.country import Country
import repositories.continent_repository as continent_repository

# create save function   
def save(country):
    # create sql query without values
    sql = "INSERT INTO countries (name, continent_id) VALUES (%s, %s) RETURNING id"
     # create list with values required by sql query
    values = [country.name, country.continent.id]
    # execute sql query
    results = run_sql(sql, values)
     # obtain id from the query result and put it into the class
    id = results[0]['id']
    country.id = id

# create select all function     
def select_all():
     # set return variable as empty list
    countries = []
    # create sql query without values
    sql = "SELECT * FROM countries"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of countries objects
    for result in results:        
        country = Country(result["name"], continent_repository.select(result['continent_id']),result["id"]) 
        countries.append(country)
    # return the result 
    return countries

# create select by id function    
def select(id):
    # create sql query without values
    sql = "SELECT * FROM countries WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    result = run_sql(sql, values)[0]
    # convert return which is a single element list of dictionaries into a continent object
    country = Country(result["name"], continent_repository.select(result['continent_id']),result["id"])
    # return the result 
    return country

# create delete all function    
def delete_all():
     # create sql query
    sql = "DELETE FROM countries"
    # execute sql query
    run_sql(sql)

# create delete by id function    
def delete(id):
    # create sql query without values
    sql = "DELETE FROM countries WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    run_sql(sql, values)
    
# create update function
    
    
    
def update(country):
    # create sql query without values
    sql = "UPDATE countries SET (name, continent_id) = (%s, %s) WHERE id = %s"
    # create list with values required by sql query
    values = [country.name,country.continent.id, country.id]
    # execute sql query
    run_sql(sql, values)