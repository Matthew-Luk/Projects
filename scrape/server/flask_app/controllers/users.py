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
    user = request.json
    print(user)
    errors = u.validate_register(user)
    if len(errors) > 0:
        return {"results": errors}
    data = {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"],
        "phone_number": user["phone_number"]
    }
    u.create_user(data)
    response = jsonify({"results": errors})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/login", methods=["POST"])
def login_user():
    errors = []
    u = Controller.get_user_repo()
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    data = request.json
    user = u.get_user_by_email(data["email"])
    print(user["password"])
    if user and not bcrypt.check_password_hash(user["password"], data["password"]):
        errors.append("The password you've entered is incorrect.")
    # if len(errors) > 0:
    #     return {"results": errors}
    # return {"results": errors}
    return user.to_json()


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
