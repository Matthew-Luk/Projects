from flask_app.configuration import Config

class Product:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.picture = data["picture"]
        self.links = []