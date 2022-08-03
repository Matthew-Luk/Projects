from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Meal:
    db = "menu"
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.type = data["type"]
        self.user = None

    @classmethod
    def save(cls,data):
        query = "INSERT INTO meals(title,description,type,user_id) VALUES(%(title)s,%(description)s,%(type)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_by_type(cls,data):
        query = "SELECT * FROM meals WHERE type = %(type)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        all_meals = []
        for row in results:
            all_meals.append(cls(row))
        return all_meals

    @classmethod
    def update_meal(cls,data):
        query = "UPDATE meals SET title=%(title)s, description=%(description)s, type=%(type)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM meals WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM meals WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        meal = cls(row)
        return meal