import psycopg2
from urllib.parse import urlparse


class Postgres:
    host: str = "localhost"
    user: str = "postgres"
    password: str = "password"
    database: str = "scrape"
    port: int = 5432

    conn: psycopg2.connection = None

    def __init__(self, uri: str = "postgres://postgres:password@localhost:5432/scrape?sslmode=disable"):
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
        if not self.conn.closed:
            self.conn.close()


def parse_uri(uri: str) -> (str, str, str, str, int):
    result = urlparse(uri)

    return (
        result.username,
        result.password,
        result.database,
        result.hostname,
        result.port
    )
