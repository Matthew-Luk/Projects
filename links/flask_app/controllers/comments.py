from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.comment import Comment

@app.route("/dashboard")
def dashboard():
    all_comments = Comment.with_users()
    return render_template("dashboard.html", all_comments = all_comments, session_id = session["user_id"])

@app.route("/add_comment")
def add_comment():
    return render_template("add_comment.html")

@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    data = {
        "comment":request.form["comment"],
        "user_id":session["user_id"]
    }
    Comment.save(data)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Comment.delete(data)
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    comment = Comment.get_by_id(data)
    return render_template("edit.html", comment = comment)

@app.route("/edit_comment", methods = ["POST"])
def update():
    Comment.edit(request.form)
    return redirect("/dashboard")