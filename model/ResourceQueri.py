import sqlite3

class LibraryQueriResource:
    def __init__(self, library):
        self.library = library
        
    def connect(self):
        self.connection = sqlite3.connect(self.library)
        self.cur = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    """Resource Queri"""

    def add_resource(self, title, category, url):
        """Agregar un nuevo recurso (libro, revista, etc.)"""
        self.connect()
        self.cur.execute("INSERT INTO Resources (title, category, url) VALUES (?, ?, ?)",
                         (title, category, url))
        self.connection.commit()
        self.disconnect()

    def get_resource_by_title_category(self, title):
        """Buscar recursos por título o categoría."""
        self.connect()
        self.cur.execute("SELECT * FROM Resources WHERE title=? ", (title,))
        resource = self.cur.fetchone()
        self.disconnect()
        return resource

    def update_resource(self, id, title, category, url):
        """Actualizar los datos de un recurso."""
        self.connect()
        self.cur.execute("UPDATE Resources SET title=?, category=?, url=? WHERE id=?",
                         (title, category, url, id))
        self.connection.commit()
        self.disconnect()

    def delete_resource(self,title):
        """Eliminar un recurso."""
        self.connect()
        self.cur.execute("DELETE FROM Resources WHERE title=?", (title,))
        self.connection.commit()
        self.disconnect()

    def get_all_resources(self):
        self.connect()
        self.cur.execute("SELECT * FROM Resources")
        resources = self.cur.fetchall()
        self.disconnect()
        return resources