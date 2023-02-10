from flask_app import app
from scrape.server.flask_app.repo.watchlists import Watchlist as WatchlistRepo
from scrape.server.flask_app.configuration import Config

@app.route("/add_to_watchlist", methods="POST")
def add_to_watchlist():
    pass