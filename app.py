from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]
        con = sqlite3.connect("questions.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO questions (col) VALUES (?)", (question,))
        con.commit()
        con.close()
        return "Your message was submitted"
    return render_template("form.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)