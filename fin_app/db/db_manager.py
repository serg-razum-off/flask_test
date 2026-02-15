import sqlite3
from fin_app.settings.config import DB_PATH


class DBManager:
    conn = None
    db_path = None

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.connect()
        return self  # SR: for with DBManager() as db:

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def _check_connection(self):
        if self.conn is None:
            raise ConnectionError(
                "Database not connected. Use 'with DBManager() as db:'"
            )

    def disconnect(self):
        self.conn.close()

    def add_user(self, name: str, email: str):
        self._check_connection()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

    def get_user(self, user_id: int):
        self._check_connection()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def update_user(self, user_id: int, name: str, email: str):
        self._check_connection()
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (name, email, user_id),
        )
        self.conn.commit()
        return cursor.fetchone()

    def delete_user(self, user_id: int):
        self._check_connection()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    # def add_transaction(self, transaction: Transaction):
    #     pass

    # def get_transaction(self, transaction_id: int):
    #     pass

    # def update_transaction(self, transaction: Transaction):
    #     pass

    # def delete_transaction(self, transaction_id: int):
    #     pass
