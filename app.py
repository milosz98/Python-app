import sqlite3
from datetime import datetime

class App:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name) # Tworzy połączenie do bazy danych o nazwie "database_name". Połączenie przechowywane jest w atrybucie "conn"
        self.cursor = self.conn.cursor() # Tworzy kursor, który będzie używany do wykonywania poleceń SQL w bazie danych. Kursor przechowywany jest w atrybucie "cursor"

        # Tworzenie tabeli
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                created_at TEXT
            )
        """) # Wykonuje polecenie SQL w bazie danych, tworząc tabelę o nazwie "entries" w przypadku jej nieistnienia. Tabela ta będzie miała kolumny: "id" (typ INTEGER, klucz główny, automatycznie inkrementowany), "title" (typ TEXT), "content" (typ TEXT) i "created_at" (typ TEXT)

        self.conn.commit() # Zatwierdza wszystkie zmiany dokonane w bazie danych. W tym przypadku, zapisuje utworzoną tabelę do bazy danych

# -------------------------------------------------------------------------------------------------------------------------------------
    
    def addEntry(self, title, content):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO entries (title, content, created_at) VALUES (?, ?, ?)", (title, content, created_at))
        self.conn.commit()