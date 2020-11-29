from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries/add")
def countries_new():
    continents = continent_repository.select_all()
    return render_template("countries/add.html", continents=continents, title="Add a country")

@countries_blueprint.route("/countries/add", methods=['POST'])
def countries_add():
    new_country = Country(request.form['name'], continent_repository.select(request.form['continent_id']))
    country_repository.save(new_country)
    return redirect('/')