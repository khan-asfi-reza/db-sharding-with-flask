import os
from dotenv import load_dotenv
import psycopg2
from uhashring import HashRing

load_dotenv()


def connect_to_postgres(db_conf):
    conn = psycopg2.connect(**db_conf)
    return conn


class DB:
    DATABASE_CLIENTS = {
        "5433": {
            "host": os.getenv("POSTGRES_HOST"),
            "port": "5433",
            "database": os.getenv("POSTGRES_DATABASE"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD")
        },
        "5434": {
            "host": os.getenv("POSTGRES_HOST"),
            "port": "5434",
            "database": os.getenv("POSTGRES_DATABASE"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD")
        },
        "5435": {
            "host": os.getenv("POSTGRES_HOST"),
            "port": "5435",
            "database": os.getenv("POSTGRES_DATABASE"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD")
        },
    }

    hash_ring = HashRing(nodes=["5433", "5434", "5435"])

    def connect_db(self, ):
        db = {}
        for client in self.DATABASE_CLIENTS:
            db[client] = connect_to_postgres(self.DATABASE_CLIENTS.get(client))

        return db

    def __init__(self):
        self.db_nodes = self.connect_db()

    def get_db(self, node: str):
        db_node = self.db_nodes.get(node, None)

        if not db_node:
            raise Exception("Invalid Database Node")

        return db_node

    def get_node(self, key):
        return self.hash_ring.get(key)["hostname"]


