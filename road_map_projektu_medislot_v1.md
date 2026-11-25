# Road Map projektu: MediSlot — Iteracja v1

## 1. Cel i granice wersji v1

* **Tytuł projektu:** MediSlot — system rezerwacji wizyt lekarskich i zarządzania harmonogramem pacjenta
* **Główny odbiorca:** Pacjent (użytkownik posiadający konto w systemie, chcący szybko sprawdzić dostępność lekarza, poznać kwotę wizyty, zarezerwować termin oraz zarządzać swoimi wizytami)
* **Najważniejszy cel v1:** Umożliwienie zalogowanemu pacjentowi przeglądania lekarzy i ich cennika, rezerwacji wolnych terminów wizyt oraz podglądu i anulowania własnych rezerwacji.
* **Konkretny efekt dla użytkownika w v1:** W pierwszej wersji użytkownik po założeniu konta i zalogowaniu może od razu zobaczyć dostępnych lekarzy, sprawdzić wolne terminy oraz poznać dokładną kwotę za każdą wizytę jeszcze przed podjęciem decyzji. Dzięki temu pacjent może w kilka kliknięć zarezerwować dogodny termin bez konieczności dzwonienia do rejestracji. Wszystkie swoje zaplanowane wizyty wraz z kwotami widzi w jednym miejscu i może je anulować, jeśli zmieni mu się plan. Efektem jest szybkie umówienie wizyty, jasna informacja o koszcie oraz pełna przejrzystość własnego harmonogramu.
* **Wybrane funkcje MVP (z Lab 01):**
  * **F01:** Rejestracja i logowanie użytkownika (konto pacjenta)
  * **F02:** Przeglądanie listy lekarzy wraz ze specjalizacją i kwotą za wizytę
  * **F03:** Przeglądanie wolnych terminów wybranego lekarza
  * **F04:** Rezerwacja wolnego terminu wizyty na koncie użytkownika
  * **F05:** Przeglądanie własnych wizyt (wraz z kwotą) oraz anulowanie rezerwacji
* **Odkładane do kolejnej iteracji (v2 / rozszerzenia):** Funkcje panelu zarządzania grafikiem i cennikiem dla lekarza/administratora (F06), zaawansowane filtrowanie po kwocie i dacie (F07), edycja danych profilu i pobieranie potwierdzenia (F08) oraz elementy poza zakresem v1 (płatności online, powiadomienia SMS/e-mail, dokumentacja medyczna).

---

## 2. Widoki — jak to ma wyglądać?

### Przegląd widoków (v1)

| ID | Nazwa widoku | Kto korzysta i w jakim celu | Powiązane dane | Powiązana funkcja |
| :--- | :--- | :--- | :--- | :--- |
| **W00** | Logowanie i rejestracja | Pacjent — aby zalogować się na istniejące konto lub założyć nowe konto użytkownika | `Użytkownik` | **F01** |
| **W01** | Lista lekarzy i terminów | Pacjent — aby wybrać lekarza, sprawdzić jego specjalizację, kwotę wizyty oraz wolne terminy i zarezerwować wizytę | `Lekarz`, `TerminWizyty`, `Wizyta` | **F02**, **F03**, **F04** |
| **W02** | Moje wizyty | Pacjent — aby sprawdzić swoje zarezerwowane wizyty, zobaczyć kwoty oraz anulować wybraną wizytę | `Wizyta`, `TerminWizyty`, `Lekarz`, `Użytkownik` | **F05** |

### Szkice widoków, przejścia (nawigacja) oraz stany sukcesu i błędów

#### W00 — Logowanie i rejestracja
* **Układ (szkic):**
  ```text
  +----------------------------------------------------------+
  |  MediSlot — Konto pacjenta                               |
  +----------------------------------------------------------+
  |  [ Logowanie ]   |   [ Rejestracja ]                     |
  +----------------------------------------------------------+
  |                                                          |
  |  Imię i nazwisko (tylko przy rejestracji):               |
  |  [ ________________________________________ ]            |
  |                                                          |
  |  E-mail:                                                 |
  |  [ ________________________________________ ]            |
  |                                                          |
  |  Hasło:                                                  |
  |  [ ________________________________________ ]            |
  |                                                          |
  |  [ Zaloguj się / Załóż konto ]                           |
  +----------------------------------------------------------+
  ```
* **Przejścia:** Po poprawnym zalogowaniu lub rejestracji przejście do **W01 (Lista lekarzy i terminów)**.
* **Dane wyświetlane i wprowadzane:** Wprowadzane: e-mail, hasło, imię i nazwisko. Wyświetlane: komunikaty walidacji i powitalne.
* **Po poprawnym działaniu:** Użytkownik jest zalogowany i trafia na widok **W01**.
* **Po błędzie:** Komunikat np. *„Nieprawidłowy e-mail lub hasło”* albo *„Konto z podanym adresem e-mail już istnieje”* (brak przejścia dalej).

#### W01 — Lista lekarzy i terminów
* **Układ (szkic):**
  ```text
  +----------------------------------------------------------+
  |  MediSlot                    Zalogowany: Jan Kowalski    |
  |  [ Lekarze i terminy ]  [ Moje wizyty ]  [ Wyloguj ]     |
  +----------------------------------------------------------+
  |  Dostępni lekarze:                                       |
  |  +----------------------------------------------------+  |
  |  | dr Anna Nowak | Dermatolog | Kwota: 200 zł         |  |
  |  | [ Pokaż terminy ]                                  |  |
  |  +----------------------------------------------------+  |
  |  | dr Piotr Lis  | Kardiolog  | Kwota: 250 zł         |  |
  |  | [ Pokaż terminy ]                                  |  |
  |  +----------------------------------------------------+  |
  |                                                          |
  |  Wolne terminy dla: dr Anna Nowak (200 zł)               |
  |  - 2026-12-03, godz. 14:30   [ Zarezerwuj ]              |
  |  - 2026-12-03, godz. 15:00   [ Zarezerwuj ]              |
  +----------------------------------------------------------+
  ```
* **Przejścia:** Kliknięcie `[ Moje wizyty ]` przenosi do **W02**; kliknięcie `[ Wyloguj ]` przenosi do **W00**; udana rezerwacja odświeża listę wolnych terminów i umożliwia przejście do **W02**.
* **Dane wyświetlane i wprowadzane:** Wyświetlane: imię i nazwisko lekarza, specjalizacja, kwota wizyty (PLN), wolne daty i godziny. Wprowadzane/wybierane: wybór lekarza oraz wybór konkretnego wolnego terminu i kliknięcie `[ Zarezerwuj ]`.
* **Po poprawnym działaniu:** Komunikat *„Wizyta została zarezerwowana”*, termin znika z puli wolnych miejsc i pojawia się w **W02**.
* **Po błędzie:** Komunikat np. *„Wybrany termin został właśnie zajęty przez innego użytkownika. Wybierz inny termin”*.

#### W02 — Moje wizyty
* **Układ (szkic):**
  ```text
  +----------------------------------------------------------+
  |  MediSlot — Moje wizyty      Zalogowany: Jan Kowalski    |
  |  [ Lekarze i terminy ]  [ Moje wizyty ]  [ Wyloguj ]     |
  +----------------------------------------------------------+
  |  Data i godzina   | Lekarz        | Kwota  | Status      |
  |  ------------------------------------------------------  |
  |  2026-12-03 14:30 | dr Anna Nowak | 200 zł | Zarezerwow. |
  |                                          [ Anuluj wizytę]|
  |  ------------------------------------------------------  |
  |  2026-11-15 10:00 | dr Piotr Lis  | 250 zł | Anulowana   |
  +----------------------------------------------------------+
  ```
* **Przejścia:** Kliknięcie `[ Lekarze i terminy ]` przenosi do **W01**; kliknięcie `[ Wyloguj ]` przenosi do **W00**.
* **Dane wyświetlane i wprowadzane:** Wyświetlane: lista wizyt przypisanych do zalogowanego pacjenta, daty, godziny, lekarze, kwoty, statusy. Wprowadzane: kliknięcie `[ Anuluj wizytę ]` przy wybranej wizycie.
* **Po poprawnym działaniu:** Status wizyty zmienia się na *„Anulowana”*, pojawia się komunikat *„Wizyta została anulowana”*, a zwolniony termin wraca jako dostępny w **W01**.
* **Po błędzie:** Komunikat np. *„Nie udało się anulować wizyty (wizyta już została anulowana lub minął jej termin)”*.

---

## 3. Struktura bazy danych — jakie dane zapisujemy?

### Tabele, pola, typy i klucze

| Tabela | Podstawowe pola i typy | Klucz główny (PK) i klucze obce (FK) |
| :--- | :--- | :--- |
| **`Użytkownik`** | `id` (liczba całkowita), `imie_nazwisko` (tekst), `email` (tekst), `haslo_hash` (tekst) | **PK:** `id` |
| **`Lekarz`** | `id` (liczba całkowita), `imie_nazwisko` (tekst), `specjalizacja` (tekst), `kwota_wizyty` (liczba zmiennoprzecinkowa / kwota) | **PK:** `id` |
| **`TerminWizyty`** | `id` (liczba całkowita), `lekarz_id` (liczba całkowita), `data_godzina` (data i godzina), `czy_wolny` (wartość logiczna) | **PK:** `id`, **FK:** `lekarz_id` -> `Lekarz.id` |
| **`Wizyta`** | `id` (liczba całkowita), `uzytkownik_id` (liczba całkowita), `termin_id` (liczba całkowita), `kwota_zapisana` (liczba zmiennoprzecinkowa / kwota), `status` (tekst) | **PK:** `id`, **FK:** `uzytkownik_id` -> `Użytkownik.id`, **FK:** `termin_id` -> `TerminWizyty.id` |

### Schemat powiązań i krotności (relacje)

```text
+---------------+          +------------------+          +------------------+          +---------------+
|  Użytkownik   | 1      N |      Wizyta      | N      1 |   TerminWizyty   | N      1 |    Lekarz     |
|---------------|----------<|------------------|----------<|------------------|----------<|---------------|
| id (PK)       |          | id (PK)          |          | id (PK)          |          | id (PK)       |
| imie_nazwisko |          | uzytkownik_id(FK)|          | lekarz_id (FK)   |          | imie_nazwisko |
| email         |          | termin_id (FK)   |          | data_godzina     |          | specjalizacja |
| haslo_hash    |          | kwota_zapisana   |          | czy_wolny        |          | kwota_wizyty  |
+---------------+          | status           |          +------------------+          +---------------+
                           +------------------+
```

* **`Lekarz (1) — (N) TerminWizyty`:** Jeden lekarz może mieć wiele terminów wizyt; każdy termin przypisany jest do jednego lekarza.
* **`Użytkownik (1) — (N) Wizyta`:** Jeden użytkownik (pacjent) może mieć wiele wizyt; każda wizyta należy do jednego użytkownika.
* **`TerminWizyty (1) — (N) Wizyta`:** Jeden termin wizyty może być powiązany z wieloma rekordami wizyt (np. w historii po anulowaniu wcześniejszej rezerwacji); każda wizyta odnosi się do jednego terminu.

---

## 4. Funkcjonalności (MVP) — co i jak ma działać?

* **F01 — Rejestracja i logowanie użytkownika**
  * **Użytkownik:** Pacjent.
  * **Oczekiwane działanie:** W widoku **W00** pacjent podaje dane do rejestracji lub logowania. System weryfikuje dane i tworzy konto w tabeli `Użytkownik` lub otwiera sesję zalogowanego użytkownika.
  * **Powiązany widok:** **W00**.
  * **Potrzebne dane:** `Użytkownik` (`id`, `imie_nazwisko`, `email`, `haslo_hash`).
  * **Warunek poprawności:** Poprawny format adresu e-mail, niepuste hasło; przy rejestracji e-mail nie istnieje jeszcze w bazie, a przy logowaniu hasło zgadza się z zapisanym kontem.
  * **Sytuacja błędna / ograniczenie:** Próba rejestracji na zajęty adres e-mail lub logowanie z błędnym hasłem kończy się komunikatem błędu i brakiem dostępu do **W01**.

* **F02 — Przeglądanie listy lekarzy wraz ze specjalizacją i kwotą**
  * **Użytkownik:** Zalogowany pacjent.
  * **Oczekiwane działanie:** W widoku **W01** system pobiera rekordy z tabeli `Lekarz` i wyświetla listę lekarzy wraz z ich specjalizacją oraz kwotą za wizytę.
  * **Powiązany widok:** **W01**.
  * **Potrzebne dane:** `Lekarz` (`id`, `imie_nazwisko`, `specjalizacja`, `kwota_wizyty`).
  * **Warunek poprawności:** W bazie istnieje co najmniej jeden lekarz z uzupełnioną kwotą wizyty ($\ge 0$), a lista poprawnie renderuje się w **W01**.
  * **Sytuacja błędna / ograniczenie:** Brak dostępnych lekarzy w systemie — wyświetlenie czytelnego komunikatu *„Brak dostępnych lekarzy”* zamiast pustego błędu aplikacji.

* **F03 — Wyświetlanie wolnych terminów wybranego lekarza**
  * **Użytkownik:** Zalogowany pacjent.
  * **Oczekiwane działanie:** Po wybraniu lekarza w **W01** system odpytuje `TerminWizyty` dla wskazanego `lekarz_id` i prezentuje terminy, w których `czy_wolny = true` (oraz z datą w przyszłości).
  * **Powiązany widok:** **W01**.
  * **Potrzebne dane:** `TerminWizyty` (`id`, `lekarz_id`, `data_godzina`, `czy_wolny`), `Lekarz` (`id`, `kwota_wizyty`).
  * **Warunek poprawności:** Wyświetlane są wyłącznie terminy oznaczone jako wolne dla wybranego lekarza.
  * **Sytuacja błędna / ograniczenie:** Brak wolnych terminów u danego lekarza — komunikat *„Brak wolnych terminów dla wybranego lekarza”*.

* **F04 — Rezerwacja wolnego terminu wizyty**
  * **Użytkownik:** Zalogowany pacjent.
  * **Oczekiwane działanie:** Pacjent w **W01** wybiera wolny termin i zatwierdza rezerwację. System tworzy nowy rekord w tabeli `Wizyta` (z przypisanym `uzytkownik_id`, `termin_id`, `kwota_zapisana` oraz statusem `Zarezerwowana`) i zmienia `czy_wolny` na `false` w `TerminWizyty`.
  * **Powiązany widok:** **W01** (oraz widoczność efektu w **W02**).
  * **Potrzebne dane:** `Użytkownik` (`id`), `TerminWizyty` (`id`, `czy_wolny`), `Lekarz` (`kwota_wizyty`), `Wizyta` (`id`, `uzytkownik_id`, `termin_id`, `kwota_zapisana`, `status`).
  * **Warunek poprawności:** Termin w chwili rezerwacji ma `czy_wolny = true`, a użytkownik jest zalogowany.
  * **Sytuacja błędna / ograniczenie:** Termin został już zarezerwowany przez kogoś innego (`czy_wolny = false`) — system blokuje duplikację i wyświetla komunikat o zajętym terminie.

* **F05 — Przeglądanie własnych wizyt i anulowanie rezerwacji**
  * **Użytkownik:** Zalogowany pacjent.
  * **Oczekiwane działanie:** W widoku **W02** pacjent widzi swoje wizyty (wraz z kwotą i statusem) i może anulować aktywną wizytę. System zmienia status wizyty na `Anulowana` w tabeli `Wizyta` oraz przywraca `czy_wolny = true` w powiązanym rekordzie `TerminWizyty`.
  * **Powiązany widok:** **W02** (oraz aktualizacja dostępności w **W01**).
  * **Potrzebne dane:** `Wizyta` (`id`, `uzytkownik_id`, `termin_id`, `kwota_zapisana`, `status`), `TerminWizyty` (`id`, `czy_wolny`), `Lekarz` (`imie_nazwisko`, `specjalizacja`).
  * **Warunek poprawności:** Wizyta należy do zalogowanego użytkownika i ma status umożliwiający anulowanie (`Zarezerwowana`).
  * **Sytuacja błędna / ograniczenie:** Próba anulowania wizyty już anulowanej lub nienależącej do zalogowanego użytkownika — system odrzuca akcję i wyświetla komunikat błędu.

---

## 5. Mapa prac dla pierwszej iteracji (v1)

| Etap / Zadanie | Osoba odpowiedzialna | Termin | Od czego zależy? | Oczekiwany rezultat |
| :--- | :--- | :--- | :--- | :--- |
| **0. Cel i zakres v1** | \[Imię Osoby 1\] i \[Imię Osoby 2\] | \[np. do 30.11.2026\] | Pomysł i MVP z Lab 01 | Uzgodniony cel v1, lista funkcji MVP i lista odłożonych funkcji |
| **1. Widoki (W00–W02)** | \[Imię Osoby 2\] | \[np. do 02.12.2026\] | Cel i zakres v1 | Lista widoków, szkice z nawigacją, opis danych oraz stanów sukcesu/błędu |
| **2. Struktura bazy danych** | \[Imię Osoby 1\] | \[np. do 04.12.2026\] | Dane potrzebne w widokach (etap 1) | Tabele, pola, typy, klucze PK/FK oraz schemat relacji |
| **3. Funkcjonalności (F01–F05)** | \[Imię Osoby 1\] i \[Imię Osoby 2\] | \[np. do 06.12.2026\] | Widoki (etap 1) i struktura bazy (etap 2) | Szczegółowy opis działania funkcji F01–F05, warunki poprawności i błędy |
| **4. Sprawdzenie spójności i zapis w repo** | \[Imię Osoby 1\] i \[Imię Osoby 2\] | \[np. przed kolejnym labem\] | Etapy 0–3 | Kompletny plik `docs/roadmap-v1.md`, link w `README.md`, wpisy na LaboChat.com i commity obu osób |

---

## 6. Kierunek kolejnej iteracji — v2

Po ocenie v1 rozpoczynamy cykl v2 od ponownej analizy widoków, następnie bazy danych i funkcjonalności:

1. **Filtrowanie wizyt według maksymalnej kwoty oraz daty**
   * **Uzasadnienie celu:** Ułatwienie pacjentowi szybkiego znalezienia konsultacji mieszczącej się w jego budżecie oraz pasującej do konkretnego przedziału czasowego.
   * **Widoki:** W **W01** dochodzi panel filtrów (`maksymalna kwota`, `data od — do`) oraz przycisk `[ Filtruj ]`.
   * **Dane:** W bazie danych **nie wymaga zmiany** (wykorzystuje istniejące pola `Lekarz.kwota_wizyty` oraz `TerminWizyty.data_godzina`).
   * **Funkcjonalności:** Rozszerzenie/nowa funkcja wyszukiwania i filtrowania dostępnych terminów po cenie i zakresie dat (odpowiednik F07 z Lab 01).

2. **Zarządzanie terminami i cennikiem przez lekarza/administratora**
   * **Uzasadnienie celu:** Umożliwienie personelowi gabinetu samodzielnego dodawania nowych wolnych slotów w kalendarzu oraz aktualizowania cen wizyt bez konieczności ręcznej ingerencji w bazę danych.
   * **Widoki:** Nowy widok **W03 (Panel grafiku i cennika)** dostępny dla roli lekarza/administratora z formularzem dodawania terminu i edycji kwoty wizyty.
   * **Dane:** W tabeli `Użytkownik` dochodzi pole `rola` (tekst: `pacjent` / `lekarz_admin`), aby rozdzielić uprawnienia w systemie.
   * **Funkcjonalności:** Funkcja dodawania nowych rekordów do `TerminWizyty` oraz aktualizacji `Lekarz.kwota_wizyty` (odpowiednik F06 z Lab 01).