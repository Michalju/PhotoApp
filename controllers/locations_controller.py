from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations/visited")
def locations_visited():
    locations = location_repository.visited()
    return render_template("locations/index.html", locations = locations, title="Visited locations")


@locations_blueprint.route("/locations/to_be_visited")
def locations_to_be_visited():
    locations = location_repository.to_be_visited()
    return render_template("locations/index.html", locations = locations, title="To be visited locations")