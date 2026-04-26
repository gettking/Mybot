from flask import Flask, request, jsonify, render_template
import sqlite3, time

app = Flask(__name__)

DB = "chat.db"

def db():
    return sqlite3.connect(DB)

# init database
def init():
    conn = db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        msg TEXT,
        time TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        name TEXT PRIMARY KEY,
        last_active REAL
    )
    """)

    conn.commit()
    conn.close()

init()

@app.route("/")
def home():
    return render_template("index.html")

# kirim pesan
@app.route("/send", methods=["POST"])
def send():
    data = request.json
    name = data.get("name")
    msg = data.get("msg")

    if not name or not msg:
        return {"status":"error"}, 400

    now = time.strftime("%H:%M")

    conn = db()
    c = conn.cursor()

    c.execute("INSERT INTO messages (name,msg,time) VALUES (?,?,?)",
              (name, msg, now))

    c.execute("INSERT OR REPLACE INTO users (name,last_active) VALUES (?,?)",
              (name, time.time()))

    conn.commit()
    conn.close()

    return {"status":"ok"}

# ambil pesan
@app.route("/messages")
def messages():
    conn = db()
    c = conn.cursor()

    c.execute("SELECT name,msg,time FROM messages ORDER BY id DESC LIMIT 100")
    data = c.fetchall()

    conn.close()

    data.reverse()

    return jsonify([
        {"name":n, "msg":m, "time":t} for (n,m,t) in data
    ])

# user online
@app.route("/online")
def online():
    now = time.time()

    conn = db()
    c = conn.cursor()

    c.execute("SELECT name,last_active FROM users")
    users = c.fetchall()

    conn.close()

    active = [u[0] for u in users if now - u[1] < 10]

    return jsonify(active)

if __name__ == "__main__":
    print("🔥 GIXN PRO RUNNING http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)
