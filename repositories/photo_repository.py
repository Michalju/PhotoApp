# Import run_sql function
from db.run_sql import run_sql

# Import photo class
from models.photo import Photo
import repositories.location_repository as location_repository

# create save function   
def save(photo):
    # create sql query without values
    sql = "INSERT INTO photos (filename, path, mine, location_id) VALUES (%s, %s, %s, %s) RETURNING id"
     # create list with values required by sql query
    values = [photo.filename, photo.path, photo.mine, photo.location.id ]
    # execute sql query
    results = run_sql(sql, values)
     # obtain id from the query result and put it into the class
    id = results[0]['id']
    photo.id = id

# create select all function     
def select_all():
     # set return variable as empty list
    photos = []
    # create sql query without values
    sql = "SELECT * FROM photos"
    # execute sql query
    results = run_sql(sql)
    # convert return which is a single element list of dictionaries into list of countries objects
    for result in results:        
        photo = Photo(result["filename"], result["path"], result["mine"], location_repository.select(result['location_id']),result["id"]) 
        photos.append(photo)
    # return the result 
    return photos

# create select by id function    
def select(id):
    # create sql query without values
    sql = "SELECT * FROM photos WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    result = run_sql(sql, values)[0]
    # convert return which is a single element list of dictionaries into a continent object
    photo = Photo(result["filename"], result["path"], result["mine"], location_repository.select(result['location_id']),result["id"]) 
    # return the result 
    return photo

# create delete all function    
def delete_all():
     # create sql query
    sql = "DELETE FROM photos"
    # execute sql query
    run_sql(sql)

# create delete by id function    
def delete(id):
    # create sql query without values
    sql = "DELETE FROM photos WHERE id = %s"
    # create list with values required by sql query
    values = [id]
    # execute sql query
    run_sql(sql, values)
    
# create update function    
def update(photo):
    # create sql query without values
    sql = "UPDATE photos SET (filename, path, mine, location_id) = (%s, %s, %s, %s) WHERE id = %s"
    # create list with values required by sql query
    values = [photo.filename, photo.path, photo.mine, photo.location.id, photo.id]
    # execute sql query
    run_sql(sql, values)

#get a single random photo for a given location

def location_photo(location):
    sql = "SELECT * FROM photos WHERE location_id = %s ORDER BY random() LIMIT 6"
    values = [location.id]
    result = run_sql(sql, values)[0]
    # convert return which is a single element list of dictionaries into a continent object
    photo = Photo(result["filename"], result["path"], result["mine"], location_repository.select(result['location_id']),result["id"]) 
    # return the result 
    return photo