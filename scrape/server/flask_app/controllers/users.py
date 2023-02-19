from flask_app import app
from scrape.server.flask_app.controllers.controllers import Controller
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask import jsonify, request

bcrypt = Bcrypt(app)
cors = CORS(app, resources={r'/register': {'origins': '*'}})

@app.route("/get_all_users")
def get_all_users():
    u = Controller.get_user_repo()
    all_users = u.get_all()
    return {"all_users": all_users}

@app.route("/register", methods=["POST"])
def register_user():
    u = Controller.get_user_repo()
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    user = request.json
    errors = u.validate_register(user)
    if len(errors) > 0:
        return {"results": errors}
    pw_hash = bcrypt.generate_password_hash(user["password"])
    data = {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": pw_hash
    }
    print(data)
    u.create_user(data)
    return {"results":errors}




@app.route("/login", methods=["POST"])
def login_user():
    u = Controller.get_user_repo()
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    user = request.json
    print(user)
    return response




# @app.route("/update/<int:id>")
# def get_user_info():
#     u = Controller.get_user_repo()
#     response = jsonify({'some': 'data'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     user = request.json
#     print(user)
#     return response

# @app.route("/update/<int:id>", methods=["POST"])
# def update_user():
#     u = Controller.get_user_repo
#     response = jsonify({'some': 'data'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     user = request.json
#     print(user)
#     return response