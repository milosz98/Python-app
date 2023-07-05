import sqlite3
from datetime import datetime

class App:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name) # Tworzy połączenie do bazy danych o nazwie "database_name". Połączenie przechowywane jest w atrybucie "conn"
        self.cursor = self.conn.cursor() # Tworzy kursor, który będzie używany do wykonywania poleceń SQL w bazie danych. Kursor przechowywany jest w atrybucie "cursor"

        # Tworzenie tabeli nagłówków
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS headers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT
            )
        """)

        # Tworzenie tabeli pozycji
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS headers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                header_id INTEGER,
                content TEXT,
                FOREIGN KEY (header_id) REFERENCES headers (id)
            )
        """)

        # Tworzenie tabeli wpisów
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS headers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                header_id INTEGER,
                item_id INTEGER,
                created_at TEXT,
                FOREIGN KEY (header_id) REFERENCES headers (id),
                FOREIGN KEY (item_id) REFERENCES items (id)
            )
        """)

        self.conn.commit() # Zatwierdza wszystkie zmiany dokonane w bazie danych

# -------------------------------------------------------------------------------------------------------------------------------------
    
    def addEntry(self, title, content): # Metoda dodająca nowy wpis do tabeli "entries" używając wartości przekazanych jako argumenty "title" i "content" oraz bieżącej daty i czasu
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Zmienna "created_at" przechowuje bieżącą datę i czas
        self.cursor.execute("INSERT INTO entries (title, content, created_at) VALUES (?, ?, ?)", (title, content, created_at)) # Wykonuje polecenie INSERT INTO w bazie danych. Wstawia nowy wpis (rekord) do tabeli "entries" z wartościami kolumn "title", "content" i "created_at". Wartości tych kolumn są przekazywane jako parametry za pomocą znaków zapytania (?), a ich rzeczywiste wartości są dostarczane jako krotka (title, content, created_at)
        self.conn.commit()

# -------------------------------------------------------------------------------------------------------------------------------------

    def display_entries(self):
        self.cursor.execute("SELECT * FROM entries") # Pobiera wszystkie kolumny (*) z tabeli "entries" i zwraca wynik w postaci kursora
        entries = self.cursor.fetchall() # Pobiera wszystkie wiersze wynikowe z kursora i przypisuje je do zmiennej entries jako listę krotek. Każda krotka reprezentuje jeden wpis z tabeli "entries"

        for entry in entries: # Iteruje po każdej krotce w liście entries, reprezentującej jeden wpis
            entry_id, title, content, createed_at = entry # Rozpakowuje wartości kolumn z krotki entry i przypisuje je do zmiennych entry_id, title, content i created_at. Każda zmienna odpowiada jednej kolumnie w tabeli "entries"
            print(f"ID: {entry_id}") # Wyświetla identyfikator wpisu
            print(f"Title: {title}")
            print(f"Content: {entry_id}")
            print(f"Created at: {entry_id}")
            print()