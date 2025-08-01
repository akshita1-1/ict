from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        number TEXT NOT NULL,
                        appointment_date TEXT NOT NULL,
                        appointment_time TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        number = request.form["number"]
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]

        
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO appointments (name, number, appointment_date, appointment_time) VALUES (?, ?, ?, ?)",
            (name, number, appointment_date, appointment_time)
        )
        conn.commit()
        conn.close()

        message = f"Thank you {name}! Your appointment is booked for {appointment_date} at {appointment_time}."
        return render_template("home.html", message=message)

    return render_template("home.html", message=None)

if __name__ == "__main__":
    app.run(debug=True)
