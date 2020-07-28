import sqlite3
from geninfo import get_website_info


class Accounts:
    def __init__(self, database_name='info.db', table_name='accounts'):
        self.name = database_name
        self.table = table_name

        # define connection and cursor
        self.conn = sqlite3.connect(self.name)
        self.cur = self.conn.cursor()
        # Create a Table
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table}('
                         'id INTEGER PRIMARY KEY, '
                         'first_name TEXT, '
                         'middle_name TEXT, '
                         'surname TEXT, '
                         'gender TEXT, '
                         'birth_year INTEGER, '
                         'adj1 TEXT, '
                         'adj2 TEXT, '
                         'location TEXT, '
                         'job TEXT, '
                         'likes TEXT, '
                         'username TEXT, '
                         'password TEXT, '
                         'made_gmail BOOLEAN DEFAULT FALSE, '
                         'enter_give_away BOOLEAN DEFAULT FALSE);')
        self.conn.commit()

    def add_account(self, data):
        self.cur.execute(f'INSERT INTO {self.table} {tuple(data.keys())} VALUES {tuple(data.values())};')
        self.conn.commit()

    def retrieve_info(self, id, kind):
        try:
            self.cur.execute(f'SELECT {kind} FROM {self.table} WHERE id = ?;', (id,))
            data = self.cur.fetchone()
            return data[0]
        except sqlite3.OperationalError:
            print(f"No such value: {kind}")

    def update_info(self, id, kind, value):
        try:
            if kind == 'id':
                raise Exception("Should not change the ID")
            self.cur.execute(f'UPDATE {self.table} SET {kind} = ? WHERE id = ?;', (value, id))
            self.conn.commit()
        except sqlite3.OperationalError:
            print(f"No such value: {kind}")

    def remove_account(self, id, password):
        self.cur.execute(f'DELETE FROM {self.table} WHERE id = ? AND number = ? AND pin = ?;', (id, card_number, pin))
        self.conn.commit()

    def close_file(self):
        self.conn.commit()
        self.cur.close()

    def dis_all(self):  # For Testing
        self.cur.execute(f'SELECT * FROM {self.table};')
        print(self.cur.fetchall())


if __name__ == "__main__":
    test = Accounts()
    #test.add_account(get_website_info())
    test.dis_all()
    print(test.retrieve_info(1, "made_gmail"))
    test.update_info(1, 'id', 2)
    test.dis_all()

