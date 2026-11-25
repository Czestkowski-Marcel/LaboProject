import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "medislot.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS Wizyta;
    DROP TABLE IF EXISTS TerminWizyty;
    DROP TABLE IF EXISTS Lekarz;
    DROP TABLE IF EXISTS Uzytkownik;

    CREATE TABLE Uzytkownik (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie_nazwisko TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        haslo_hash TEXT NOT NULL
    );

    CREATE TABLE Lekarz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie_nazwisko TEXT NOT NULL,
        specjalizacja TEXT NOT NULL,
        kwota_wizyty REAL NOT NULL CHECK (kwota_wizyty >= 0)
    );

    CREATE TABLE TerminWizyty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lekarz_id INTEGER NOT NULL,
        data_godzina TEXT NOT NULL,
        czy_wolny INTEGER NOT NULL DEFAULT 1,
        FOREIGN KEY (lekarz_id) REFERENCES Lekarz(id) ON DELETE CASCADE
    );

    CREATE TABLE Wizyta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uzytkownik_id INTEGER NOT NULL,
        termin_id INTEGER NOT NULL,
        kwota_zapisana REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'Zarezerwowana',
        FOREIGN KEY (uzytkownik_id) REFERENCES Uzytkownik(id) ON DELETE CASCADE,
        FOREIGN KEY (termin_id) REFERENCES TerminWizyty(id) ON DELETE CASCADE
    );
    """)

    # Użytkownik demonstracyjny nr 1 (hasło: haslo123)
    cur.execute(
        "INSERT INTO Uzytkownik (imie_nazwisko, email, haslo_hash) VALUES (?, ?, ?)",
        ("Jan Kowalski (Demo)", "jan@medislot.pl", generate_password_hash("haslo123"))
    )

    # Przykładowi lekarze i kwoty wizyt
    lekarze = [
        ("dr n. med. Anna Nowak", "Dermatolog", 220.00),
        ("lek. Piotr Zieliński", "Kardiolog", 280.00),
        ("lek. Katarzyna Wiśniewska", "Internista", 160.00),
    ]
    cur.executemany(
        "INSERT INTO Lekarz (imie_nazwisko, specjalizacja, kwota_wizyty) VALUES (?, ?, ?)",
        lekarze
    )

    # Przykładowe wolne terminy (daty w przyszłości)
    terminy = [
        (1, "2026-12-03 10:00", 1),
        (1, "2026-12-03 14:30", 1),
        (1, "2026-12-04 09:15", 1),
        (2, "2026-12-03 16:00", 1),
        (2, "2026-12-05 11:30", 1),
        (3, "2026-12-02 08:30", 1),
        (3, "2026-12-02 12:00", 1),
    ]
    cur.executemany(
        "INSERT INTO TerminWizyty (lekarz_id, data_godzina, czy_wolny) VALUES (?, ?, ?)",
        terminy
    )

    conn.commit()
    conn.close()
    print("Baza medislot.db została zainicjalizowana pomyślnie.")


if __name__ == "__main__":
    init_db()