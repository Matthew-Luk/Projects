from scrape.server.flask_app.models import Product as ProductModel
from scrape.server.flask_app.models import Postgres
from scrape.server.flask_app.configuration import Config

class Product:
    postgres_uri: str = ""
    postgres: Postgres = None

    def __init__(self, config: Config):
        self.postgres_uri = config.POSTGRES_URL
        self.postgres = Postgres(config.POSTGRES_URL)