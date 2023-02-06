from flask_app import app
from scrape.server.flask_app.repo import User as UserModel
from scrape.server.flask_app.configuration import Config

@app.route("/get_all_users")
def get_all_users():
    config = Config()
    u = UserModel(config)
    all_users = u.get_all()
    return {"all_users": all_users}