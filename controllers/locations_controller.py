from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository
import repositories.country_repository as country_repository

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations/visited")
def locations_visited():
    locations = location_repository.visited()
    return render_template("locations/index.html", locations = locations, title="Visited locations")


@locations_blueprint.route("/locations/to_be_visited")
def locations_to_be_visited():
    locations = location_repository.to_be_visited()
    return render_template("locations/index.html", locations = locations, title="To be visited locations")

@locations_blueprint.route("/locations/add")
def locations_new():
    countries = country_repository.select_all()
    return render_template("locations/add.html", countries=countries, title="Add a location")

@locations_blueprint.route("/locations/add", methods=['POST'])
def locations_add():
    new_location = Location(request.form['name'], request.form['description'], request.form['visited'], country_repository.select(request.form['country_id']))
    location_repository.save(new_location)
    return redirect('/')