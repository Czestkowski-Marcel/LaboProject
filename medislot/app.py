import os
import sqlite3
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "medislot-lokalny-klucz-v1"
DB_NAME = "medislot.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Zaloguj się, aby uzyskać dostęp do tej strony.", "error")
            return redirect(url_for("auth"))
        return f(*args, **kwargs)
    return decorated


# W00 + F01: Logowanie i rejestracja
@app.route("/", methods=["GET", "POST"])
def auth():
    if "user_id" in session:
        return redirect(url_for("lekarze"))

    if request.method == "POST":
        akcja = request.form.get("akcja")
        email = request.form.get("email", "").strip().lower()
        haslo = request.form.get("haslo", "")

        if not email or "@" not in email or not haslo:
            flash("Podaj poprawny adres e-mail oraz hasło.", "error")
            return redirect(url_for("auth"))

        conn = get_db()
        if akcja == "rejestracja":
            imie_nazwisko = request.form.get("imie_nazwisko", "").strip()
            if not imie_nazwisko:
                conn.close()
                flash("Podaj imię i nazwisko.", "error")
                return redirect(url_for("auth"))
            try:
                cur = conn.execute(
                    "INSERT INTO Uzytkownik (imie_nazwisko, email, haslo_hash) VALUES (?, ?, ?)",
                    (imie_nazwisko, email, generate_password_hash(haslo))
                )
                conn.commit()
                session["user_id"] = cur.lastrowid
                session["user_name"] = imie_nazwisko
                conn.close()
                flash("Konto zostało utworzone. Witamy w MediSlot!", "success")
                return redirect(url_for("lekarze"))
            except sqlite3.IntegrityError:
                conn.close()
                flash("Konto z podanym adresem e-mail już istnieje.", "error")
                return redirect(url_for("auth"))

        elif akcja == "logowanie":
            user = conn.execute(
                "SELECT * FROM Uzytkownik WHERE email = ?", (email,)
            ).fetchone()
            conn.close()
            if user and check_password_hash(user["haslo_hash"], haslo):
                session["user_id"] = user["id"]
                session["user_name"] = user["imie_nazwisko"]
                flash("Zalogowano pomyślnie.", "success")
                return redirect(url_for("lekarze"))
            else:
                flash("Nieprawidłowy e-mail lub hasło.", "error")
                return redirect(url_for("auth"))

    return render_template("auth.html")


@app.route("/wyloguj")
def wyloguj():
    session.clear()
    flash("Wylogowano z systemu.", "success")
    return redirect(url_for("auth"))


# W01 + F02 + F03: Lista lekarzy, kwoty i wolne terminy
@app.route("/lekarze")
@login_required
def lekarze():
    wybrany_lekarz_id = request.args.get("lekarz_id", type=int)
    conn = get_db()
    lista_lekarzy = conn.execute("SELECT * FROM Lekarz ORDER BY specjalizacja, imie_nazwisko").fetchall()

    wybrany_lekarz = None
    wolne_terminy = []
    if wybrany_lekarz_id:
        wybrany_lekarz = conn.execute(
            "SELECT * FROM Lekarz WHERE id = ?", (wybrany_lekarz_id,)
        ).fetchone()
        if wybrany_lekarz:
            wolne_terminy = conn.execute(
                "SELECT * FROM TerminWizyty WHERE lekarz_id = ? AND czy_wolny = 1 ORDER BY data_godzina",
                (wybrany_lekarz_id,)
            ).fetchall()

    conn.close()
    return render_template(
        "lekarze.html",
        lekarze=lista_lekarzy,
        wybrany_lekarz=wybrany_lekarz,
        wolne_terminy=wolne_terminy
    )


# F04: Rezerwacja wolnego terminu wizyty
@app.route("/rezerwuj", methods=["POST"])
@login_required
def rezerwuj():
    termin_id = request.form.get("termin_id", type=int)
    if not termin_id:
        flash("Nie wybrano terminu wizyty.", "error")
        return redirect(url_for("lekarze"))

    conn = get_db()
    termin = conn.execute("""
        SELECT t.id, t.lekarz_id, t.czy_wolny, l.kwota_wizyty
        FROM TerminWizyty t
        JOIN Lekarz l ON t.lekarz_id = l.id
        WHERE t.id = ?
    """, (termin_id,)).fetchone()

    if not termin:
        conn.close()
        flash("Wybrany termin nie istnieje.", "error")
        return redirect(url_for("lekarze"))

    if termin["czy_wolny"] != 1:
        conn.close()
        flash("Wybrany termin został właśnie zajęty przez innego użytkownika. Wybierz inny termin.", "error")
        return redirect(url_for("lekarze", lekarz_id=termin["lekarz_id"]))

    conn.execute(
        "INSERT INTO Wizyta (uzytkownik_id, termin_id, kwota_zapisana, status) VALUES (?, ?, ?, 'Zarezerwowana')",
        (session["user_id"], termin["id"], termin["kwota_wizyty"])
    )
    conn.execute("UPDATE TerminWizyty SET czy_wolny = 0 WHERE id = ?", (termin["id"],))
    conn.commit()
    conn.close()

    flash("Wizyta została zarezerwowana!", "success")
    return redirect(url_for("moje_wizyty"))


# W02 + F05: Przeglądanie własnych wizyt i anulowanie
@app.route("/moje-wizyty")
@login_required
def moje_wizyty():
    conn = get_db()
    wizyty = conn.execute("""
        SELECT w.id, w.kwota_zapisana, w.status, t.data_godzina,
               l.imie_nazwisko AS lekarz_nazwa, l.specjalizacja
        FROM Wizyta w
        JOIN TerminWizyty t ON w.termin_id = t.id
        JOIN Lekarz l ON t.lekarz_id = l.id
        WHERE w.uzytkownik_id = ?
        ORDER BY t.data_godzina DESC
    """, (session["user_id"],)).fetchall()
    conn.close()
    return render_template("moje_wizyty.html", wizyty=wizyty)


@app.route("/anuluj/<int:wizyta_id>", methods=["POST"])
@login_required
def anuluj(wizyta_id):
    conn = get_db()
    wizyta = conn.execute(
        "SELECT * FROM Wizyta WHERE id = ? AND uzytkownik_id = ?",
        (wizyta_id, session["user_id"])
    ).fetchone()

    if not wizyta or wizyta["status"] != "Zarezerwowana":
        conn.close()
        flash("Nie udało się anulować wizyty (wizyta już anulowana lub brak uprawnień).", "error")
        return redirect(url_for("moje_wizyty"))

    conn.execute("UPDATE Wizyta SET status = 'Anulowana' WHERE id = ?", (wizyta_id,))
    conn.execute("UPDATE TerminWizyty SET czy_wolny = 1 WHERE id = ?", (wizyta["termin_id"],))
    conn.commit()
    conn.close()

    flash("Wizyta została anulowana, a termin wrócił do puli wolnych miejsc.", "success")
    return redirect(url_for("moje_wizyty"))


if __name__ == "__main__":
    if not os.path.exists(DB_NAME):
        from init_db import init_db
        init_db()
    app.run(debug=True)