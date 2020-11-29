from flask import Flask, render_template
from controllers.locations_controller import locations_blueprint
from controllers.countries_controller import countries_blueprint
import repositories.location_repository as location_repository
app = Flask(__name__)

app.register_blueprint(locations_blueprint)
app.register_blueprint(countries_blueprint)

@app.route("/")
def main():
    locations = location_repository.select_six_random()
    return render_template("locations/index.html", locations = locations, title="Welcome to the photo locations app")

if __name__ == '__main__':
    app.run()