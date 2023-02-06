from scrape.server.flask_app.models import User as UserModel
from scrape.server.flask_app.models import Postgres
from scrape.server.flask_app.configuration import Config
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Use https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
class User:
    postgres_uri: str = ""
    postgres: Postgres = None

    def __init__(self, config: Config):
        self.postgres_uri = config.POSTGRES_URL
        self.postgres = Postgres(config.POSTGRES_URL)

    def get_all(self):
        cursor = self.postgres.conn.cursor()
        query = """SELECT * FROM users"""
        cursor.execute(query)
        self.postgres.conn.commit()
        record = cursor.fetchall()
        print(record)
        cursor.close()
        return record

    def get_user_by_id(self, user_id: str):
        cursor = self.postgres.conn.cursor()
        cursor.execute("""SELECT * FROM users WHERE id = %s""", (user_id,))
        self.postgres.conn.commit()
        record = cursor.fetchone()
        print(record)
        cursor.close()

    def get_user_by_email(self, email: str):
        cursor = self.postgres.conn.cursor()
        query = """SELECT * FROM users WHERE email = %s"""
        cursor.execute(query, (email,))
        self.postgres.conn.commit()
        record = cursor.fetchone()
        print(record)
        cursor.close()

    def create_user(self):
        cursor = self.postgres.conn.cursor()
        query = """ INSERT INTO users (name, email, phone) VALUES (%s,%s,%s)"""
        cursor.execute(query, ("test", "test@gmail.com", "415-312-2819"))
        self.postgres.conn.commit()
        count = cursor.rowcount
        cursor.close()

    def edit_user_by_id(
            self,
            email: str = "",
            phone_number: str = "",
            password: str = ""):
        cursor = self.postgres.conn.cursor()

        query = ""
        if email != "":
            # TODO: query for updating email using user_id
            query = ""
        elif phone_number != "":
            # TODO: query for updating phone_number using user_id
            query = ""
        elif password != "":
            # TODO: query for updating password using user_id
            query = ""
        else:
            raise Exception("No changes detected when attempting to update user information.")

        cursor.execute(query)
        self.postgres.conn.commit()
        count = cursor.rowcount
        cursor.close()

    def delete_user_by_id(self):
        cursor = self.postgres.conn.cursor()
        cursor.execute()
        self.postgres.conn.commit()
        count = cursor.rowcount
        cursor.close()

    def delete_user_by_email(self):
        cursor = self.postgres.conn.cursor()
        cursor.execute()
        self.postgres.conn.commit()
        count = cursor.rowcount
        cursor.close()

    def validate_register(self, first_name: str, last_name: str, email: str, password: str):
        is_valid = True
        if not EMAIL_REGEX.match(email):
            flash("Invalid Email Address")
            is_valid = False
        if len(first_name) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(last_name) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(password) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

    # def validate_register(user):
    #     is_valid = True
    #     user_in_db = User.get_user_by_email(user)
    #     if user_in_db:
    #         flash("Email is associated with another account")
    #         is_valid = False
    #     if not EMAIL_REGEX.match(user["email"]):
    #         flash("Invalid Email Address")
    #         is_valid = False
    #     if len(user["first_name"]) < 3:
    #         flash("First name must be at least 3 characters.")
    #         is_valid = False
    #     if len(user["last_name"]) < 3:
    #         flash("Last name must be at least 3 characters.")
    #         is_valid = False
    #     if len(user["password"]) < 8:
    #         flash("Password must be at least 8 characters.")
    #         is_valid = False
    #     if user["password"] != user["confirm_password"]:
    #         flash("Passwords do not match!")
    #         is_valid = False
    #     return is_valid


if __name__ == "__main__":
    config = Config()
    config.POSTGRES_URL = "postgres://postgres:password@localhost:5432/scrape"

    # how to use create_user() when it isn't static
    user = User(config)
    user.create_user()

    # how to use create_user() when it is static
    User.create_user()