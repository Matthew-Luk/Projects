from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Comment:
    db = "linktree"
    def __init__(self,data):
        self.id = data["id"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users = None

    @classmethod
    def with_users(cls):
        query = "SELECT * FROM comments JOIN users ON users.id = user_id"
        results = connectToMySQL(cls.db).query_db(query)
        if len(results) < 1:
            return False
        all_comments = []
        for row in results:
            comment = cls(row)
            i = {
                "id":row["users.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["users.created_at"],
                "updated_at":row["users.updated_at"]
            }
            comment.users = User(i)
            all_comments.append(comment)
        return all_comments

    @classmethod
    def save(cls,data):
        query = "INSERT INTO comments(comment,user_id) VALUES(%(comment)s,%(user_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM comments WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        comment = cls(row)
        return comment

    @classmethod
    def edit(cls,data):
        query = "UPDATE comments SET comment=%(comment)s;"
        return connectToMySQL(cls.db).query_db(query,data)