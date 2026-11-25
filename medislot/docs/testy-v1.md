# Plan i wyniki sprawdzenia wersji v1 — MediSlot

## 1. Ocena spójności kodu z mapą v1 (`docs/roadmap-v1.md`)
* **Widoki:** Zaimplementowano wszystkie 3 widoki (`W00` w `templates/auth.html`, `W01` w `templates/lekarze.html`, `W02` w `templates/moje_wizyty.html`) wraz ze wspólną nawigacją w `base.html` i komunikatami `flash`.
* **Struktura bazy:** Skrypt `init_db.py` tworzy dokładnie 4 tabele (`Uzytkownik`, `Lekarz`, `TerminWizyty`, `Wizyta`) z kluczami głównymi `PK`, kluczami obcymi `FK` oraz aktywnym `PRAGMA foreign_keys = ON`.
* **Funkcjonalności MVP:** Wszystkie 5 funkcji (`F01`–`F05`) działa po stronie serwera z użyciem zapytań parametryzowanych SQL.
* **Braki / odłożone do v2:** Zgodnie z założeniami v1 brak filtrowania po cenie/dacie oraz brak panelu edycji grafiku przez lekarza (zaplanowane na v2).

## 2. Scenariusze testowe i rzeczywiste wyniki

| ID | Funkcja | Scenariusz i dane wejściowe | Kroki wykonania | Oczekiwany wynik | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | **F01** | Rejestracja nowego pacjenta (`Anna Testowa`, `anna@test.pl`, `tajne123`) | 1. Otwórz W00.<br>2. Wypełnij formularz rejestracji i kliknij *Załóż konto*. | Utworzenie rekordu w `Uzytkownik`, zalogowanie i przekierowanie do W01 z komunikatem sukcesu. | **działa** |
| **T02** | **F01** | Próba rejestracji na zajęty e-mail (`jan@medislot.pl`) | 1. W W00 wpisz istniejący e-mail `jan@medislot.pl`.<br>2. Kliknij *Załóż konto*. | Odrzucenie zapisu i wyświetlenie komunikatu błędu o zajętym adresie e-mail. | **działa** |
| **T03** | **F01** | Logowanie błędnym hasłem (`jan@medislot.pl` / `zlehaslo`) | 1. W W00 wpisz błędne hasło i kliknij *Zaloguj się*. | Brak dostępu do W01 i komunikat *Nieprawidłowy e-mail lub hasło*. | **działa** |
| **T04** | **F02 / F03** | Przeglądanie lekarzy, kwot i wolnych terminów | 1. Zaloguj się jako `jan@medislot.pl`.<br>2. Kliknij *Pokaż terminy* przy wybranym lekarzu. | Wyświetlenie listy lekarzy z kwotami oraz lista wolnych terminów wybranego specjalisty. | **działa** |
| **T05** | **F04** | Rezerwacja wolnego terminu wizyty | 1. W W01 wybierz wolny termin i kliknij *Zarezerwuj*. | Dodanie wizyty w `Wizyta`, oznaczenie terminu jako zajętego (`czy_wolny = 0`) i wyświetlenie wizyty w W02. | **działa** |
| **T06** | **F04** | Próba ponownej rezerwacji tego samego (zajętego) terminu | 1. Otwórz W01 w drugiej karcie/sesji przed odświeżeniem i kliknij *Zarezerwuj* dla zajętego już terminu. | Blokada duplikacji rezerwacji na serwerze i komunikat, że termin został już zajęty. | **działa** |
| **T07** | **F05** | Anulowanie własnej rezerwacji | 1. Przejdź do W02.<br>2. Kliknij *Anuluj wizytę* przy aktywnej rezerwacji. | Zmiana statusu wizyty na `Anulowana` w W02 oraz ponowne pojawienie się terminu jako wolnego w W01. | **działa** |
| **T08** | **Baza** | Trwałość danych po restarcie serwera | 1. Zarezerwuj wizytę.<br>2. Zatrzymaj serwer (`Ctrl+C`) i uruchom ponownie (`flask --app app run`).<br>3. Zaloguj się i sprawdź W02. | Zarezerwowana wizyta nadal jest widoczna na koncie użytkownika w W02. | **działa** |