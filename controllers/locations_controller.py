from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository
import repositories.country_repository as country_repository
import repositories.photo_repository as photo_repository
import requests
import json

locations_blueprint = Blueprint("locations", __name__)

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
    return render_template("locations/add.html", countries=countries, title="Add a location")

@locations_blueprint.route("/locations/add", methods=['POST'])
def locations_add():
    new_location = Location(request.form['name'], request.form['description'], request.form['visited'], country_repository.select(request.form['country_id']))
    location_repository.save(new_location)
    return redirect('/locations/view')

@locations_blueprint.route("/locations/api_test")
def api_new():
    return render_template("locations/api_test.html", title="API test")

@locations_blueprint.route("/locations/api_test", methods=['POST'])
def locations_api_result():
# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=da62419a0afbc1c0263202a88657c615
    # api_result = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
    # api_result = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=da62419a0afbc1c0263202a88657c615")
    api_result = requests.get("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=57.149651&lon=-2.099075&dt=1614034829&appid=da62419a0afbc1c0263202a88657c615")
    # request.form['api_address']
    api_result_json = json.dumps(api_result.json() , sort_keys=True, indent=4)
    return render_template("/locations/api_results.html", api_result=api_result_json)

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
    updated_location = Location(request.form['location_name'], request.form['location_description'], request.form['location_visited'], country ,request.form['location_id'])
    location_repository.update(updated_location)
    return redirect('/locations/view')


@locations_blueprint.route("/locations/view_single/<id>")
def locations_view_single(id):
    pass
    location=location_repository.select(id)
    photos = photo_repository.select_all_for_location(id)
    return render_template("locations/view_single.html", location=location, photos=photos,  title=location.name)