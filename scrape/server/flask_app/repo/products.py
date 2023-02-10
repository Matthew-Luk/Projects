from scrape.server.flask_app.models import Product as ProductModel
from scrape.server.flask_app.models import Postgres
from scrape.server.flask_app.configuration import Config

class Product:
    postgres_uri: str = ""
    postgres: Postgres = None

    def __init__(self, config: Config):
        self.postgres_uri = config.POSTGRES_URL
        if config.POSTGRES_URL == "":
            self.postgres = Postgres()
        else:
            self.postgres = Postgres(config.POSTGRES_URL)

    def get_top_searches(self):
        cursor = self.postgres.conn.cursor()
        query = """SELECT * FROM products ORDER BY likes DESC LIMIT 4"""
        cursor.execute(query)
        self.postgres.conn.commit()
        record = cursor.fetchall()
        print(record)
        cursor.close()
        return record