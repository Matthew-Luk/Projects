from scrape.server.flask_app.models.watchlist import Watchlist as WatchlistModel
from scrape.server.flask_app.models import Postgres
from scrape.server.flask_app.configuration import Config

class Watchlist:
    postgres_uri: str = ""
    postgres: Postgres = None

    def __init__(self, config: Config):
        self.postgres_uri = config.POSTGRES_URL
        if config.POSTGRES_URL == "":
            self.postgres = Postgres()
        else:
            self.postgres = Postgres(config.POSTGRES_URL)

    def add_to_watchlist():
        pass