from flask import Flask
from main.controllers import postcodes_uk

app = Flask(__name__)


def get_app(config) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)

    flask_app.register_blueprint(postcodes_uk.app)
    return flask_app


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )
