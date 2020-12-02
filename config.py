import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SCSS_STATIC_DIR = os.path.join(basedir, "app ", "static", "css")
    SCSS_ASSET_DIR = os.path.join(basedir, "app", "assets", "scss")

    APP_URL_PREFIX = ""

    AGGREGATOR_URL = "https://dts-aggregator.herokuapp.com"
    AGGREGATOR_COLLECTIONS_ENDPOINT = "/collections"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    @staticmethod
    def init_app(app):
        app.debug = True


class TestConfig(Config):
    pass


config = {"dev": DevelopmentConfig, "prod": Config, "test": TestConfig}
