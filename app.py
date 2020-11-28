from flask import Flask, render_template
from controllers.locations_controller import locations_blueprint

app = Flask(__name__)

app.register_blueprint(locations_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()