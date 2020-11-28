from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations/visited")
def locations_visited():
    locations = location_repository.visited()
    return render_template("locations/visited.html", locations = locations)