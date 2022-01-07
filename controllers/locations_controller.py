from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from flask import Blueprint
from flask import current_app
from models.location import Location
from werkzeug.utils import secure_filename
import repositories.location_repository as location_repository
import repositories.country_repository as country_repository
import repositories.photo_repository as photo_repository
from models.file import File
from models.photo import Photo
import requests
import json
import imghdr
import os
import pdb

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@locations_blueprint.route("/locations/visited")
def locations_visited():
    locations = photo_repository.locations_photo(location_repository.visited())
    return render_template("locations/index.html", locations = locations, title="Visited locations")


@locations_blueprint.route("/locations/to_be_visited")
def locations_to_be_visited():
    locations = photo_repository.locations_photo(location_repository.to_be_visited())
    return render_template("locations/index.html", locations = locations, title="To be visited locations")

@locations_blueprint.route("/locations/new")
def locations_new():
    countries = country_repository.select_all()
    return render_template("locations/add.html", countries=countries, title="Add a location", country_id_default="")


@locations_blueprint.route("/locations/add", methods=['POST'])
def locations_add():
    new_location = Location(request.form['name'], request.form['description'], request.form['visited'], request.form['latitude'], request.form['longitude'], country_repository.select(request.form['country_id']))
    location_repository.save(new_location)
    file = request.files['files']
    if file.filename != '': 
        uploaded_files = request.files.getlist('files')
        for uploaded_file in uploaded_files:
            Added_photo = File(new_location ,uploaded_file,current_app.config['UPLOAD_PATH'])
            photo_repository.save(Photo(Added_photo._file_name_with_extension, True, new_location))

    return redirect('/locations/view')

@locations_blueprint.route("/locations/api_test")
def api_new():
    return render_template("locations/api_test.html", title="API test")

@locations_blueprint.route("/locations/api_test", methods=['POST'])
def locations_api_result():

    #api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    #api_result = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=" + current_app.config['WEATHER_API'])
    api_result = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=57.316747&lon=-2.482072&units=metric&APPID=" + current_app.config['WEATHER_API'])
    api_result_json = json.dumps(api_result.json() , sort_keys=True, indent=4)
    #pdb.set_trace()
    return render_template("/locations/api_results.html", api_result=api_result.json())

@locations_blueprint.route("/locations/view")
def locations_view():
    locations = location_repository.select_all()
    return render_template("locations/view.html", locations=locations, title="List of locations")

@locations_blueprint.route("/locations/delete", methods=['POST'])
def locations_delete():
    location_repository.delete(request.form['location_id'])
    return redirect('/locations/view')

@locations_blueprint.route("/locations/edit", methods=['POST'])
def locations_edit():
    location=location_repository.select(request.form['location_id'])
    countries = country_repository.select_all()
    return render_template("locations/edit.html", location = location, countries = countries, title="Edit/Delete location")

@locations_blueprint.route("/locations/update", methods=['POST'])
def locations_update():
    country = country_repository.select(request.form['country_id'])
    updated_location = Location(request.form['location_name'], request.form['location_description'], request.form['location_visited'], request.form['latitude'], request.form['longitude'], country ,request.form['location_id'])
    location_repository.update(updated_location)
    return redirect('/locations/view')


@locations_blueprint.route("/locations/view_single/<id>")
def locations_view_single(id):
    pass
    location=location_repository.select(id)
    photos = photo_repository.select_all_for_location(id)
    return render_template("locations/view_single.html", location=location, photos=photos,  title=location.name)