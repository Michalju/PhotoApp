# Import run_sql function
from db.run_sql import run_sql

# Import continent class
from models.continent import Continent

# create save function   
def save(continent):
    # create sql query without values
    sql = "INSERT INTO continents (name) VALUES (%s) RETURNING id"
     # create list with values required by sql query
    values = [continent.name]
    # execute sql query
    results = run_sql(sql, values)
     # obtain id from the query result and put it into the class
    id = results[0]['id']
    continent.id = id

# create select all function     
def select_all():
     # set return variable as empty list
    continents = []
    # create sql query without values
    sql = "SELECT * FROM continents"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of continents objects
    for result in results:        
        continent = Continent(result["name"],result["id"]) 
        continents.append(continent)
    # return the result 
    return continents

# create select by id function    
def select(id):
    # create sql query without values
    sql = "SELECT * FROM continents WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    result = run_sql(sql, values)[0]
    # convert return which is a single element list of dictionaries into a continent object
    continent = Continent(result["name"],result["id"])
    # return the result 
    return continent

# create delete all function    
def delete_all():
     # create sql query
    sql = "DELETE FROM continents"
    # execute sql query
    run_sql(sql)

# create delete by id function    
def delete(id):
    # create sql query without values
    sql = "DELETE FROM continents WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    run_sql(sql, values)
    
# create update function
    
    
    
def update(continent):
    # create sql query without values
    sql = "UPDATE continents SET name = %s WHERE id = %s"
    # create list with values required by sql query
    values = [continent.name, continent.id]
    # execute sql query
    run_sql(sql, values)