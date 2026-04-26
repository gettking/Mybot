from flask import Flask, render_template, request, redirect, session, send_from_directory
from flask_socketio import SocketIO, emit
import os, uuid, random

app = Flask(__name__)
app.secret_key = "gixn_secret"

socketio = SocketIO(app, async_mode="threading")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

users = {}

def get_color(name):
    if name not in users:
        users[name] = f"#{random.randint(0,0xFFFFFF):06x}"
    return users[name]

# LOGIN
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pw = request.form.get("pw")

        if pw == "@123":
            session["user"] = user
            return redirect("/chat")

    return render_template("login.html")

# CHAT PAGE
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect("/")
    return render_template("chat.html", user=session["user"])

# UPLOAD
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    ext = file.filename.split(".")[-1]
    filename = str(uuid.uuid4()) + "." + ext

    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    return {"url": "/file/" + filename}

@app.route("/file/<name>")
def file(name):
    return send_from_directory(UPLOAD_FOLDER, name)

# SOCKET
@socketio.on("msg")
def handle_msg(data):
    name = data["user"]
    msg = data["msg"]

    emit("message", {
        "user": name,
        "msg": msg,
        "color": get_color(name)
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
