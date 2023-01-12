import psycopg2


class Postgres:
    def __init__(self,
                host: str = "localhost",
                user: str = "postgres",
                password: str = "password",
                database: str = "scrape",
                port: int = 5432):
        try:
            conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        except:
            print("I am unable to connect to the database")
