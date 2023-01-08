class Item:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.picture = data["picture"]
        self.links = None