# Prompty i decyzje projektowe — MediSlot v1

## Narzędzie AI i przebieg pracy
* **Wybrany czat AI:** Gemini (Google — wariant bezpłatny w przeglądarce).
* **Sposób pracy:** Iteracyjne generowanie kodu zgodnie z cyklem z Lab 02: najpierw dobór technologii (P1), następnie szkielet aplikacji i widoki W00–W02 (P2–P3), podpięcie trwałej bazy SQLite (P4), implementacja logiki F01–F05 (P5) oraz weryfikacja testami (P7).

## Zastosowane prompty (P1–P7)

### P1 — Wybór technologii
> Pracujemy we dwoje nad projektem MediSlot – system rezerwacji wizyt lekarskich. Cel v1: umożliwienie zalogowanemu pacjentowi przeglądania lekarzy i ich cennika, rezerwacji wolnych terminów wizyt oraz podglądu i anulowania własnych rezerwacji. Widoki: W00 Logowanie i rejestracja, W01 Lista lekarzy i terminów, W02 Moje wizyty. Dane: Użytkownik, Lekarz, TerminWizyty, Wizyta. Funkcje MVP: F01–F05. Zaproponuj dwa proste zestawy technologii do uruchomienia lokalnie bez płatnych usług. Wyjaśnij role składników, wybierz prostszy wariant i uzasadnij go.

**Decyzja zespołu:** Wybraliśmy wariant **Python 3 + Flask + SQLite + HTML/CSS**, ponieważ pozwala uruchomić aplikację jednym poleceniem bez stawiania osobnego serwera bazy danych.

### P2 & P3 — Szkielet aplikacji i widoki W00, W01, W02
> Przygotuj szkielet lokalnego MediSlot v1: HTML/CSS, Python 3, Flask i SQLite przez sqlite3. Plik startowy: app.py. Dopasuj widoki do szkiców: W00 (logowanie/rejestracja), W01 (lista lekarzy ze specjalizacją i kwotą oraz lista wolnych terminów), W02 (tabela moich wizyt z przyciskiem anulowania). Dodaj nawigację oraz komunikaty sukcesu i błędów.

### P4 — Trwała baza danych SQLite
> Dodaj SQLite przez sqlite3 zgodnie z mapą: Uzytkownik(id, imie_nazwisko, email, haslo_hash), Lekarz(id, imie_nazwisko, specjalizacja, kwota_wizyty), TerminWizyty(id, lekarz_id, data_godzina, czy_wolny), Wizyta(id, uzytkownik_id, termin_id, kwota_zapisana, status). Włącz kontrolę kluczy obcych (PRAGMA foreign_keys = ON), używaj zapytań parametryzowanych i dodaj skrypt init_db.py z użytkownikiem demo nr 1 oraz przykładowymi lekarzami.

### P5 — Implementacja funkcjonalności F01–F05
> Zaimplementuj funkcje MVP F01–F05: rejestrację i logowanie z hashowaniem haseł, wyświetlanie lekarzy i wolnych terminów, rezerwację wolnego terminu z blokadą podwójnego zapisu (czy_wolny = 0) oraz anulowanie własnej wizyty z przywróceniem terminu do puli wolnych (czy_wolny = 1).

## Własne poprawki i wnioski zespołu
1. **Zapis historycznej kwoty wizyty (`kwota_zapisana`):** Podczas weryfikacji kodu zwróciliśmy uwagę, że tabela `Wizyta` powinna zapisywać kwotę obowiązującą w momencie rezerwacji (`kwota_zapisana`), aby ewentualna zmiana cennika lekarza w przyszłości nie zmieniała kosztu już umówionych wizyt.
2. **Automatyczna inicjalizacja przy pierwszym starcie:** Dodaliśmy w `app.py` warunek sprawdzający istnienie pliku `medislot.db`, aby aplikacja nie zwracała błędu `no such table`, jeśli ktoś zapomni uruchomić `python init_db.py` przed startem serwera.
3. **Bezpieczeństwo haseł:** Zastosowaliśmy funkcje `generate_password_hash` i `check_password_hash` z biblioteki `werkzeug.security` (wbudowanej we Flask), dzięki czemu hasła w bazie SQLite nie są przechowywane jawnym tekstem.