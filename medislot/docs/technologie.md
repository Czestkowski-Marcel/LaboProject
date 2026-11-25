# Wybrane technologie i narzędzia — MediSlot v1

## Uzasadnienie wyboru
Dla pierwszej wersji aplikacji **MediSlot** wybraliśmy zestaw oparty na języku Python 3, mikroframeworku Flask, lokalnej bazie danych SQLite oraz standardowych technologiach webowych HTML5 i CSS3. Taki stos technologiczny jest lekki, darmowy i nie wymaga instalowania zewnętrznych serwerów bazodanowych ani płatnych usług chmurowych, co gwarantuje łatwe uruchomienie projektu na komputerach obu członków zespołu. Flask zapewnia prostą obsługę tras (routingu), sesji logowania pacjenta oraz walidację formularzy rezerwacji bez zbędnego narzutu konfiguracyjnego. Wbudowany w Pythona moduł `sqlite3` pozwala na szybkie utworzenie relacyjnej bazy danych w pojedynczym pliku lokalnym z pełną obsługą kluczy głównych i obcych. Warstwa prezentacji oparta na szablonach Jinja2, czystym HTML i CSS umożliwia przejrzyste odwzorowanie widoków W00, W01 i W02 bez konieczności nauki skomplikowanych frameworków frontendowych. Całość uzupełnia system kontroli wersji Git oraz platforma GitHub, które ułatwiają nam równoległą pracę i śledzenie postępów.

## Zestawienie narzędzi i ról w projekcie

| Obszar | Wybrana technologia | Wersja | Rola w projekcie |
| :--- | :--- | :--- | :--- |
| **Widoki (Frontend)** | HTML5, CSS3, szablony Jinja2 | HTML5 / CSS3 | Struktura widoków W00–W02, formularze logowania i rezerwacji, wyświetlanie listy lekarzy, kwot i komunikatów. |
| **Serwer (Backend)** | Python 3 + Flask | Python 3.11+ / Flask 3.x | Obsługa żądań HTTP, zarządzanie sesją zalogowanego pacjenta, logika rezerwacji oraz walidacja dostępności terminów. |
| **Baza danych** | SQLite (`sqlite3`) | SQLite 3 | Trwały zapis użytkowników, lekarzy, cenników, dostępnych terminów oraz zarezerwowanych wizyt w lokalnym pliku `medislot.db`. |
| **Praca zespołu** | VS Code, Git, GitHub, LaboChat | Git 2.x | Edycja kodu, historia zmian (commity), podział zadań oraz weryfikacja spójności projektu. |
| **Wsparcie AI** | Gemini (Google) | Plan darmowy | Generowanie szkieletu kodu, zapytań SQL, walidacji serwerowej oraz scenariuszy testowych na podstawie mapy v1. |