from flask import Flask, render_template, request
from controllers.locations_controller import locations_blueprint
from controllers.countries_controller import countries_blueprint
import repositories.location_repository as location_repository
import repositories.photo_repository as photo_repository
app = Flask(__name__)

app.register_blueprint(locations_blueprint)
app.register_blueprint(countries_blueprint)
app.config['MAX_CONTENT_LENGTH'] = 100*1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/photos'

@app.route("/")
def main():
    locations = photo_repository.locations_photo(location_repository.select_six_random())
    return render_template("locations/index.html", locations = locations, title="Welcome to the photo locations app")

@app.route("/search" , methods=['POST'])
def search():
    locations = photo_repository.locations_photo(location_repository.search(request.form['search'])) 
    return render_template("locations/index.html", locations = locations, title=f"Search result for: {request.form['search']}")

if __name__ == '__main__':
    app.run()