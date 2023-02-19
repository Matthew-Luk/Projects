from flask_app.configuration import Config
from scrape.server.flask_app.models import Product as ProductModel

class Watchlist:
    def __init__(self,data):
        self.user_id = data["user_id"]
        self.products: list[ProductModel] = []

    def save(self):
        pass

    def get_watchlist(self,data):
        pass