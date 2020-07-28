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
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table} ('
                         'id INTEGER, '
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
        #for key, value in data.items():
            #print(key, value)
        self.cur.execute(f'INSERT INTO {self.table} VALUES 1;')
        self.conn.commit()

    def retrieve_info(self, kind):
        pass

    def remove_account(self, full_name, password):
        pass

    def close_file(self):
        self.conn.commit()
        self.cur.close()

    def dis_all(self):  # For Testing
        self.cur.execute(f'SELECT * FROM {self.table};')
        print(self.cur.fetchall())


if __name__ == "__main__":
    test = Accounts()
    test.add_account(get_website_info())
    test.dis_all()
