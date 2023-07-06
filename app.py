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
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                header_id INTEGER,
                content TEXT,
                FOREIGN KEY (header_id) REFERENCES headers (id)
            )
        """)

        # Tworzenie tabeli wpisów
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
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
    
    def addEntry(self, header_title, item_content): # Metoda dodająca nowy wpis do tabeli "entries" używając wartości przekazanych jako argumenty "title" i "content" oraz bieżącej daty i czasu
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Zmienna "created_at" przechowuje bieżącą datę i czas
        
        # Dodawanie nagłówka
        self.cursor.execute("INSERT INTO headers (title) VALUES (?)", (header_title,)) # Dodaje nowy nagłówek z wartością kolumny "title" pobraną z argumentu header_title. Wartość kolumny jest przekazywana jako parametr za pomocą znaku zapytania (?), a jej rzeczywista wartość jest dostarczana jako krotka (header_title,)
        header_id = self.cursor.lastrowid

        # Dodawanie pozycji
        self.cursor.execute("INSERT INTO items (header_id, content) VALUES (?, ?)", (header_id, item_content))
        item_id = self.cursor.lastrowid

        # Dodawanie wpisu
        self.cursor.execute("INSERT INTO entries (header_id, item_id, created_at) VALUES (?, ?, ?)", (header_id, item_id, created_at))
        self.conn.commit()

        #self.cursor.execute("INSERT INTO entries (title, content, created_at) VALUES (?, ?, ?)", (title, content, created_at)) # Wykonuje polecenie INSERT INTO w bazie danych. Wstawia nowy wpis (rekord) do tabeli "entries" z wartościami kolumn "title", "content" i "created_at". Wartości tych kolumn są przekazywane jako parametry za pomocą znaków zapytania (?), a ich rzeczywiste wartości są dostarczane jako krotka (title, content, created_at)
        #self.conn.commit()

# -------------------------------------------------------------------------------------------------------------------------------------

    def displayEntries(self):
        self.cursor.execute("SELECT * FROM entries") # Pobiera wszystkie kolumny (*) z tabeli "entries" i zwraca wynik w postaci kursora
        entries = self.cursor.fetchall() # Pobiera wszystkie wiersze wynikowe z kursora i przypisuje je do zmiennej entries jako listę krotek. Każda krotka reprezentuje jeden wpis z tabeli "entries"

        for entry in entries: # Iteruje po każdej krotce w liście entries, reprezentującej jeden wpis
            entry_id, title, content, created_at = entry # Rozpakowuje wartości kolumn z krotki entry i przypisuje je do zmiennych entry_id, title, content i created_at. Każda zmienna odpowiada jednej kolumnie w tabeli "entries"
            print(f"ID: {entry_id}") # Wyświetla identyfikator wpisu
            print(f"Title: {title}") # Wyświetla tytuł wpisu
            print(f"Content: {content}") # Wyświetla treść wpisu
            print(f"Created at: {created_at}") # Wyświetla datę i czas utworzenia wpisu
            print() # Wyświetla pusty wiersz, żeby oddzielić kolejne wpisy od siebie

# -------------------------------------------------------------------------------------------------------------------------------------

    def processData(self, data): # "data" reprezentuje dane wejściowe
        for header_title, item_content in data: # Iteracja po elementach "data", które są krotkami, przypisując wartości do zmiennych "header_title" oraz "item_content". Zakładamy, że każda krotka w "data" zawiera parę wartości: tytuł nagłówka (header_title) i treść pozycji (item_content)
            self.addEntry(header_title, item_content) # Wywołanie metody "addEntry" z przekazanymi argumentami "header_title" oraz "item_content". Metoda addEntry jest odpowiedzialna za dodanie wpisu do bazy danych na podstawie przekazanych informacji o nagłówku i pozycji

        self.displayEntries() # "displayEntries" jest odpowiedzialny za wyświetlenie wszystkich wpisów z bazy danych w terminalu

# -------------------------------------------------------------------------------------------------------------------------------------

app = App("jakasbaza.db")

data = [("Nagłówek 1", "Pozycja 1"), ("Nagłówek 2", "Pozycja 2")]

app.processData(data)

app.displayEntries()

app.addEntry("Nagłówek 3", "Pozycja 3")