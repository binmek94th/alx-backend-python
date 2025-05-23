import sqlite3

class ExecuteQuery:
    def __init__(self, query, **kwargs):
        self.conn = None
        self.query = query
        self.cursor = None
        self.kwargs = kwargs

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, tuple(self.kwargs.values()))
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


query = "SELECT * FROM users WHERE age > ?"

with ExecuteQuery(query, age=25) as cursor:
    results = cursor.fetchall()
    for row in results:
        print(row)
