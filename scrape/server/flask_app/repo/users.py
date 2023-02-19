from scrape.server.flask_app.models import User as UserModel
from scrape.server.flask_app.models import Postgres
from scrape.server.flask_app.configuration import Config
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Use https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
class User:
    postgres_uri: str = ""
    postgres: Postgres = None

    def __init__(self, config: Config):
        self.postgres_uri = config.POSTGRES_URL
        if config.POSTGRES_URL == "":
            self.postgres = Postgres()
        else:
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
        return record

    def create_user(self, user: dict):
        cursor = self.postgres.conn.cursor()
        query = """INSERT INTO users (first_name, last_name, email, password) VALUES (%s,%s,%s,%s)"""
        cursor.execute(query, (user["first_name"], user["last_name"], user["email"], user["password"],))
        self.postgres.conn.commit()
        count = cursor.rowcount
        cursor.close()
        return count

    def edit_user_by_id(
            self,
            first_name: str = "",
            last_name: str = "",
            email: str = "",
            password: str = ""):
        cursor = self.postgres.conn.cursor()

        query = ""
        if first_name != "":
            # TODO: query for updating first_name using user_id
            query = ""
        elif last_name != "":
            # TODO: query for updating last_name using user_id
            query = ""
        elif email != "":
            # TODO: query for updating email using user_id
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

    # Possibility for edit function
    # def edit_user_by_id(self, id: int, first_name: str, last_name: str, email: str, password: str):
    #     cursor = self.postgres.conn.cursor()
    #     query = """UPDATE users SET first_name = %s, last_name = %s, email = %s, password = %s WHERE id = %s"""
    #     cursor.execute(query, (id, first_name, last_name, email, password,))
    #     self.postgres.conn.commit()
    #     count = cursor.rowcount
    #     cursor.close()

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

    def validate_register(self, user: dict):
        error = []
        user_in_db = self.get_user_by_email(email = user["email"])
        if user_in_db != None:
            error.append("Email is associated with another account.")
        if not EMAIL_REGEX.match(user["email"]):
            error.append("Email is invalid.")
        if len(user["first_name"]) < 3:
            error.append("First name must be at least 3 characters.")
        if len(user["last_name"]) < 3:
            error.append("Last name must be at least 3 characters.")
        if len(user["password"]) < 8:
            error.append("Password must be at least 8 characters")
        if user["password"] != user["confirm_password"]:
            error.append("Passwords must match")
        return error

    def validate_login(self, user: dict):
        error = "True"
        user_in_db = User.get_by_email(user)
        if not user_in_db:
            error = "Email is not associated with an account!"
        elif not EMAIL_REGEX.match(user["email"]):
            error = "Invalid Email Address"
        elif len(user["password"]) < 8:
            error = "Password must be at least 8 characters."
        return error

if __name__ == "__main__":
    config = Config()
    config.POSTGRES_URL = "postgres://postgres:password@localhost:5432/scrape"

    # how to use create_user() when it isn't static
    user = User(config)
    user.create_user()

    # how to use create_user() when it is static
    User.create_user()
