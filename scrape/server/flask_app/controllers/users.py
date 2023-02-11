from flask_app import app
from scrape.server.flask_app.controllers.controllers import Controller

@app.route("/get_all_users")
def get_all_users():
    u = Controller.get_user_repo()
    all_users = u.get_all()
    return {"all_users": all_users}
