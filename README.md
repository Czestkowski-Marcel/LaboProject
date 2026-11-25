MediSlot – system rezerwacji wizyt lekarskich i zarządzania harmonogramem pacjenta
Zespół
Nazwa zespołu: CodeMed
Osoba 1: Bartłomiej Milinkiewicz, nr indeksu: 180600, GitHub: @Milin600
Osoba 2: Marcel Czestkowski, nr indeksu: 180583, GitHub: @czestkowski-marcel
Grupa laboratoryjna: I IO

Idea i problem
Umawianie wizyt lekarskich w prywatnych gabinetach oraz małych przychodniach wciąż często odbywa się telefonicznie, co generuje długie kolejki na infolinii i utrudnia pacjentom szybkie sprawdzenie dostępności specjalistów. Obecnie pacjent musi dzwonić w określonych godzinach pracy rejestracji, dopytywać o wolne daty oraz ręcznie zapisywać terminy i koszty konsultacji. Dodatkowo brak jednego, przejrzystego miejsca z historią wizyt oraz informacjami o cenach usług powoduje nieporozumienia finansowe i częste zapominanie o zaplanowanych konsultacjach. Strona MediSlot rozwiązuje ten problem, przenosząc cały proces rezerwacji i zarządzania wizytami do prostego systemu webowego dostępnego przez całą dobę. Z rozwiązania będą korzystać przede wszystkim pacjenci poszukujący szybkiego dostępu do lekarzy oraz personel administracyjny zarządzający grafikiem gabinetu. W ramach systemu użytkownik zakłada własne konto, przegląda listę dostępnych specjalistów wraz z przejrzystym cennikiem i wybiera dogodny termin z kalendarza. Każdy termin ma przypisaną konkretną kwotę, dzięki czemu pacjent jeszcze przed potwierdzeniem rezerwacji zna dokładny koszt usługi. W panelu użytkownika pacjent może w dowolnej chwili sprawdzić swoje nadchodzące wizyty, przejrzeć historię poprzednich spotkań oraz dokonać anulacji lub zmiany terminu. Dzięki wdrożeniu aplikacji pacjenci zyskują pełną kontrolę nad swoim kalendarzem zdrowotnym i oszczędzają czas poświęcany na kontakt telefoniczny. Z kolei placówka medyczna minimalizuje liczbę pustych okienek w grafiku oraz automatyzuje obsługę zapisów.

Użytkownicy i scenariusz
Główna grupa odbiorców: Pacjenci (osoby chcące szybko umówić wizytę lekarską online i kontrolować wydatki na leczenie) oraz administratorzy/lekarze (zarządzający dostępnymi terminami i cennikiem usług).
Przykładowy scenariusz użycia:
Pacjent wchodzi na stronę MediSlot i loguje się na swoje konto użytkownika (lub dokonuje szybkiej rejestracji).
Wybiera z listy interesującą go specjalizację (np. dermatolog), a system wyświetla dostępnych lekarzy, wolne terminy oraz kwotę za konsultację (np. 200 zł).
Pacjent klika wybrany termin (np. czwartek, godz. 14:30) i zatwierdza rezerwację.
Wizyta natychmiast pojawia się w zakładce „Moje wizyty” na koncie pacjenta wraz z datą, godziną, nazwiskiem lekarza oraz kwotą do zapłaty w gabinecie, a wybrany termin znika z puli wolnych miejsc dla innych użytkowników.
Zakres funkcjonalny
ID
Funkcjonalność
Zakres
F01
Użytkownik może założyć konto pacjenta oraz zalogować się do systemu.
MVP
F02
Użytkownik może przeglądać listę lekarzy wraz z ich specjalizacją oraz ceną (kwotą) za wizytę.
MVP
F03
Użytkownik może wyświetlić kalendarz z dostępnymi, wolnymi terminami dla wybranego lekarza.
MVP
F04
Użytkownik może zarezerwować wybrany wolny termin wizyty, przypisując go do swojego konta.
MVP
F05
Użytkownik może przeglądać listę swoich zaplanowanych i historycznych wizyt wraz z podsumowaniem kwot oraz anulować nadchodzącą wizytę.
MVP
F06
Użytkownik (administrator/lekarz) może dodawać nowe wolne terminy do grafiku oraz edytować cennik wizyt.
Rozszerzenie
F07
Użytkownik może filtrować i wyszukiwać terminy według maksymalnej kwoty wizyty oraz przedziału dat.
Rozszerzenie
F08
Użytkownik może edytować dane swojego profilu (np. numer telefonu, adres e-mail) oraz pobrać potwierdzenie rezerwacji.
Rozszerzenie

Poza zakresem
Płatności online (bramki płatnicze): W pierwszej wersji kwota wizyty ma charakter informacyjny i jest rozliczana bezpośrednio w gabinecie – system nie obsługuje przelewów, BLIK-a ani kart płatniczych.
Automatyczne powiadomienia SMS i e-mail: System nie wysyła zewnętrznych przypomnień na telefon ani skrzynkę pocztową przed wizytą (status wizyt widoczny jest wyłącznie po zalogowaniu w panelu użytkownika).
Dokumentacja medyczna i e-recepty: Aplikacja służy wyłącznie do zarządzania terminami i kosztami wizyt – nie przechowuje wyników badań, historii chorób ani wystawionych recept.
Organizacja współpracy
Podział zadań:
[Imię Osoby 1]: Architektura bazy danych, logika rezerwacji terminów i obsługa kont użytkowników (Backend), konfiguracja repozytorium GitHub.
[Imię Osoby 2]: Interfejs użytkownika, widok kalendarza i listy wizyt (Frontend), prowadzenie przestrzeni zespołu w LaboChat.com i dokumentacji.
(Uwaga: Obie osoby wspólnie odpowiadają za aktualność pliku README.md oraz znajomość całej koncepcji projektu).
Sposób kontaktu: Bieżąca komunikacja za pośrednictwem platformy LaboChat.com oraz szybkie konsultacje na [np. Discord / Messenger].
Zasada zapisywania i aktualizowania ustaleń: Wszystkie kluczowe decyzje projektowe oraz zadania zapisujemy w przestrzeni zespołu na LaboChat.com. Wszelkie zmiany w dokumentacji i kodzie wprowadzamy przez repozytorium GitHub, opisując każdy commit w sposób jasno wskazujący, co zostało dodane lub poprawione.
Odnośniki
Repozytorium GitHub: https://github.com/Czestkowski-Marcel/LaboProject
Przestrzeń projektu w LaboChat.com: 

## Dokumentacja projektu
* [Road Map v1](medislot/docs/roadmap-v1.md)
* [Wybrane technologie](medislot/docs/technologie.md)
* [Prompty i decyzje v1](medislot/docs/prompty-v1.md)
* [Plan i wyniki testów v1](medislot/docs/testy-v1.md)

## Uruchomienie aplikacji lokalnie (v1)

### Wymagania
* Python 3.10 lub nowszy

### Krok po kroku — Windows (PowerShell)
```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe init_db.py
.\.venv\Scripts\python.exe -m flask --app app run

Krok po kroku — macOS / Linux
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python init_db.py
.venv/bin/python -m flask --app app run

Po uruchomieniu otwórz w przeglądarce adres: http://127.0.0.1:5000

