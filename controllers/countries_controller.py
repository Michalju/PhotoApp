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
    return redirect('/countries/view')

@countries_blueprint.route("/countries/view")
def countries_view():
    countries = country_repository.select_all()
    return render_template("countries/view.html", countries=countries, title="List of countries")

@countries_blueprint.route("/countries/delete", methods=['POST'])
def countries_delete():
    country_repository.delete(request.form['country_id'])
    return redirect('/countries/view')


@countries_blueprint.route("/countries/edit", methods=['POST'])
def countries_edit():
    country=country_repository.select(request.form['country_id'])
    continents = continent_repository.select_all()
    return render_template("countries/edit.html", country = country, continents = continents, title="Edit/Delete country")

@countries_blueprint.route("/countries/update", methods=['POST'])
def countries_update():
    continent = continent_repository.select(request.form['continent_id'])
    updated_country = Country(request.form['country_name'], continent ,request.form['country_id'])
    country_repository.update(updated_country)
    return redirect('/countries/view')