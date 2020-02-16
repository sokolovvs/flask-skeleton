from flask import Flask
from src.app import App
from src.exceptions.domain_exceptions.entity.entity_not_found_exception import EntityNotFoundException
from src.exceptions.domain_exceptions.entity.validation.entity_validation_exception import EntityValidationException
from src.exceptions.domain_exceptions.improve_domain_exception import DomainException
from src.exceptions.domain_exceptions.security.base_security_exception import BaseSecurityException

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(exception):
    code = 500

    if isinstance(exception, DomainException):
        if isinstance(exception, EntityNotFoundException):
            code = 404
        elif isinstance(exception, BaseSecurityException):
            code = 403
        elif isinstance(exception, EntityValidationException):
            code = 422

        return jsonify(errors=str(exception)), code

    if App.is_production_env():
        return jsonify(errors='Unknown error'), code

    raise exception


with app.app_context():
    from src.routes.api import *
    from src.routes.web import *


def init_app(app: Flask):
    app = App(app)
    app.load_config()
    app.start()


if __name__ == "__main__":
    init_app(app)
