import sqlite3

# Basic database class to connect to the SQLite file.
class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)