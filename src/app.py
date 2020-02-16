from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class App:
    __db = None
    __app = None

    def __init__(self, app: Flask) -> None:
        App.__app = app
        App.__init_db(app)

    @staticmethod
    def __init_db(app: Flask):
        App.__db = SQLAlchemy(app)

    @staticmethod
    def get_db() -> SQLAlchemy:
        return App.__db

    @staticmethod
    def get_app() -> Flask:
        return App.__app

    def start(self, port='5000', host='127.0.0.1', debug=True) -> 'App':
        self.__app.run(debug=debug, port=port, host=host)

        return self

    def load_config(self) -> 'App':
        self.__app.config['SECRET_KEY'] = 'a really really really really long secret key'
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db-sokolov:db-123QWEasd1@localhost/blog_flask'
        self.__app.config['APP_ENV'] = 'local'

        return self

    @staticmethod
    def get_config():
        return App.get_app().config

    @staticmethod
    def is_production_env() -> bool:
        return App.get_config().get('APP_ENV') == 'production'
