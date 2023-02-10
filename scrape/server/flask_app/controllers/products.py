from flask_app import app
from scrape.server.flask_app.repo.products import Product as ProductRepo
from scrape.server.flask_app.configuration import Config

@app.route("/top_searches")
def top_searches():
    config = Config()
    p = ProductRepo(config)
    top_searches = p.get_top_searches()
    return {"top_searches": top_searches}