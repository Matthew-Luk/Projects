from flask_app import app
from scrape.server.flask_app.controllers.controllers import Controller

@app.route("/top_searches")
def top_searches():
    p = Controller.get_product_repo()
    top_searches = p.get_top_searches()
    return {"top_searches": top_searches}