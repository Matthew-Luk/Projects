from flask import render_template, redirect, request, session, flash
from flask_app.models.meal import Meal
from flask_app import app

@app.route("/add")
def add():
    return render_template("add_a_meal.html")

@app.route("/add_meal", methods=["POST"])
def add_meal():
    data = {
        "title":request.form["title"],
        "description":request.form["description"],
        "type":request.form["type"],
        "user_id":session["user_id"]
    }
    Meal.save(data)
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit_meal(id):
    data = {
        "id":id
    }
    return render_template("edit_meal.html", meal = Meal.get_by_id(data))

@app.route("/update/<int:id>", methods=["POST"])
def update_meal(id):
    data = {
        "id":id,
        "title":request.form["title"],
        "description":request.form["description"],
        "type":request.form["type"],
        "user_id":session["user_id"]
    }
    Meal.update_meal(data)
    return redirect("/dashboard")

@app.route("/snacks")
def snacks():
    data = {
        "type":["snack"]
    }
    return render_template("snacks.html", all_snacks = Meal.get_all_by_type(data))

@app.route("/eating_out")
def eating_out():
    data = {
        "type":["takeout"]
    }
    return render_template("eating_out.html", all_takeout_meals = Meal.get_all_by_type(data))

@app.route("/eating_at_home")
def eating_at_home():
    data = {
        "type":["home"]
    }
    return render_template("eating_at_home.html", all_home_meals = Meal.get_all_by_type(data))

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Meal.delete(data)
    return redirect("/dashboard")