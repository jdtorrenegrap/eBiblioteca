import sqlite3

class VirtualDBLibrary:

    def __init__(self, library):
        self.library = library

    def connect(self):
        self.connection = sqlite3.connect(self.library)
        self.cur = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def create_users(self):
        self.connect()
        self.cur.execute('''CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            user_type TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        self.disconnect()

    def create_resources(self):
        self.connect()
        self.cur.execute('''CREATE TABLE Resources (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            category TEXT,
            url TEXTz,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        self.disconnect()



if __name__ == "__main__":
    try:
        data = VirtualDBLibrary('library.db')
        data.create_users()
        data.create_resources()
        print("Éxito")

    except Exception as e:
        print("Error:", e)