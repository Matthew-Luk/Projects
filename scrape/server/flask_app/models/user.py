from scrape.server.flask_app.configuration import Config

class User:
    def __init__(self,data):
        # Required fields
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

        # Optional fields
        self.phone_number = data.get("phone_number", "000-000-0000")

        # Auto generated fields
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]