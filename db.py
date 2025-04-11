import sqlite3
from datetime import datetime

class PageDatabase:
    def __init__(self, db_name='crawler.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                title TEXT,
                status_code INTEGER,
                depth INTEGER,
                fetched_at TEXT
            )
        ''')
        self.conn.commit()

    def insert_page(self, url, title, status_code, depth):
        try:
            self.conn.execute('''
                INSERT INTO pages (url, title, status_code, depth, fetched_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (url, title, status_code, depth, datetime.utcnow().isoformat()))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass  # URL already exists

    def close(self):
        self.conn.close()
