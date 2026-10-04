import sqlite3
from contextlib import contextmanager


class LocalDataBase():
    def __init__(self, archive_name="techlog.db"):
        self.archive_name = archive_name
        self.initialize_db()

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.archive_name)
        try:
            yield connection
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    def initialize_db(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                telephone TEXT NOT NULL
                )
            ''')
        print("Database initialized")
