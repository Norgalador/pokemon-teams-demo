from flask_app import app
from flask_app.controllers import team_controller, user_controller, pokemon_controller

if __name__ == "__main__":
    app.run(debug=True, port=5001)