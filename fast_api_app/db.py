import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()


def db_conn():
    try:
        # Connect to an existing database
        conn = psycopg2.connect(
            host=os.getenv("host"),
            dbname=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            port=os.getenv("port"),
            cursor_factory=RealDictCursor,
        )
        # Open a cursor to perform database operations
        print("Database connected")
        return conn.cursor()
    except Exception as error:
        print("Connecting to database unsuccessful")
        print("Error:", error)
        # Consider re-raising the exception or implementing a retry logic
        raise
