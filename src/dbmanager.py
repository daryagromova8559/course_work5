import psycopg2

from src.config import config


class DBManager:
    def __init__(self):
        self.db_name = 'hh_company'

    def execute_(self, query):
        conn = psycopg2.connect(dbname=self.db_name, **config())
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
        conn.close()
        return results