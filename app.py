import sqlite3

class App:
    def __init__(self):
        pass

    def createTable(): # Metoda służąca do tworzenia tabeli w bazie danych

        conn = sqlite3.connect('wpisy.db') # Stworzenie nowej bazy danych (lub połączenie się z już istniejącą)
        c = conn.cursor() # Utworzenie kursora umożliwiającego wykonanie poleceń SQL na bazie danych, np. wstawianie danych, pobieranie danych itp.

        # Utworzenie tabeli "wpisy"
        c.execute("""CREATE TABLE IF NOT EXISTS wpisy
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        tresc TEXT NOT NULL) """) # Ta linia wykonuje polecenie SQL w celu utworzenia tabeli o nazwie 'wpisy'. Tabela ta będzie miała dwa kolumny: id (typu INTEGER z kluczem głównym) oraz tresc (typu TEXT, nie może być pusta). Jeśli tabela już istnieje, to instrukcja CREATE TABLE IF NOT EXISTS zapewnia, że nie zostanie utworzona ponownie
        
        # Zatwierdzenie zmian i zamknięcie połączenia z bazą danych
        conn.commit() # Ta linia zatwierdza zmiany wprowadzone w bazie danych. W tym przypadku, potwierdza utworzenie tabeli
        conn.close() # Zamyka połączenie z bazą danych

    # OGÓLNIE: Ten fragment kodu tworzy tabelę 'wpisy' w bazie danych o nazwie 'wpisy.db'. Jeśli tabela już istnieje, to instrukcja CREATE TABLE IF NOT EXISTS zapewnia, że nie zostanie utworzona ponownie.