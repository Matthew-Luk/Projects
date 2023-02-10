import psycopg2
from urllib.parse import urlparse


class Postgres:
    host: str = "localhost"
    user: str = "postgres"
    password: str = "password"
    database: str = "scrape"
    port: int = 5432

    conn = None

    def __init__(self, uri: str = "postgres://postgres:password@localhost:5432/scrape?sslmode=disable"):
        # set default postgres uri to one that hits docker postgres
        if uri == "": uri = "postgres://postgres:password@localhost:5432/scrape?sslmode=disable"
        self.user, self.password, self.database, self.host, self.port = parse_uri(uri)

        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
        except:
            print("I am unable to connect to the database")

    def __del__(self):
        # close the DB connection when we're finished
        if self.conn and not self.conn.closed:
            self.conn.close()


# Example uri string: "postgres://postgres:password@localhost:5432/scrape?sslmode=disable"
def parse_uri(uri: str) -> (str, str, str, str, int):
    result = urlparse(uri)
    database = result.path.split("/")[1]  # "/scrape" -> ["", "scrape"]

    return (
        result.username,
        result.password,
        database,
        result.hostname,
        result.port
    )
