import hashlib
import sqlite3

class LibraryQueriesUser:
    def __init__(self, library):
        self.library = library
        
    def connect(self):
        self.connection = sqlite3.connect(self.library)
        self.cur = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    
    """User Queries"""

    def create_user(self, name, email, password, user_type):
        """Crear nuevo Usuario"""
        self.connect()
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        self.cur.execute(
            "INSERT INTO Users (name, email, password, user_type) VALUES (?, ?, ?, ?)",
            (name, email, encrypted_password, user_type)
        )
        self.connection.commit()
        self.disconnect()
        
    def user_exists(self, email, password):
        """Verificar si un usuario existe"""
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        self.connect()
        self.cur.execute("SELECT * FROM Users WHERE email=? AND password=?", (email, encrypted_password))
        user = self.cur.fetchone()
        self.disconnect()
        return user is not None

    def get_user_by_email(self,email):
        """Bucar a usuario por email"""
        self.connect()
        self.cur.execute("SELECT * FROM Users WHERE email=?",(email,))
        user = self.cur.fetchone()
        self.disconnect()
        return user
    
    def update_user(self, id, name, email, password, user_type, registration_date):
        """Actualizar usuario"""
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        self.connect()
        self.cur.execute("UPDATE Users SET name=?, email=?, password=?, user_type=?, registration_date=? WHERE id=?",
                         (name, email, encrypted_password, user_type, registration_date, id))
        self.connection.commit()
        self.disconnect()

    def delete_user(self, id):
        """Eliminar usuario"""
        self.connect()
        self.cur.execute("DELETE FROM Users WHERE id=?", (id,))
        self.connection.commit()
        self.disconnect()

    
    def get_all_user(self):
        """Todos los usuarios"""
        self.connect()
        self.cur.execute("SELECT * FROM Users")
        users = self.cur.fetchall()
        self.disconnect()
        return users
        
    def get_users_by_type(self, user_type):
        self.connect()
        self.cur.execute("SELECT * FROM Users WHERE user_type=?", (user_type,))
        users = self.cur.fetchall()
        self.disconnect()
        return users