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
    
    def addEntry(self, title, content): # Metoda dodająca nowy wpis do tabeli "entries" używając wartości przekazanych jako argumenty "title" i "content" oraz bieżącej daty i czasu
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Zmienna "created_at" przechowuje bieżącą datę i czas
        self.cursor.execute("INSERT INTO entries (title, content, created_at) VALUES (?, ?, ?)", (title, content, created_at)) # Wykonuje polecenie INSERT INTO w bazie danych. Wstawia nowy wpis (rekord) do tabeli "entries" z wartościami kolumn "title", "content" i "created_at". Wartości tych kolumn są przekazywane jako parametry za pomocą znaków zapytania (?), a ich rzeczywiste wartości są dostarczane jako krotka (title, content, created_at)
        self.conn.commit()