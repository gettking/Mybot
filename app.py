from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import time

app = Flask(__name__)
CORS(app)

# =========================
# DATABASE SIMULASI
# =========================
wallets = {}

# =========================
# HOME ROUTE (FIX NOT FOUND)
# =========================
@app.route("/")
def home():
    return "🚀 L1 WALLET SERVER ACTIVE"

# =========================
# GENERATE ADDRESS
# =========================
def gen_address():
    return "TTM" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# =========================
# CREATE WALLET
# =========================
@app.route("/create_wallet", methods=["POST"])
def create_wallet():
    data = request.json

    if not data:
        return jsonify({"error": "no data"})

    addr = gen_address()

    wallets[addr] = {
        "username": data.get("username"),
        "password": data.get("password"),
        "balance": 0,
        "last_faucet": 0
    }

    return jsonify({"address": addr})

# =========================
# FAUCET (10 TTM / 12 JAM)
# =========================
@app.route("/faucet", methods=["POST"])
def faucet():
    addr = request.json.get("address")

    if addr not in wallets:
        return jsonify({"error": "wallet not found"})

    now = time.time()

    if now - wallets[addr]["last_faucet"] < 43200:
        return jsonify({"error": "cooldown"})

    wallets[addr]["balance"] += 10
    wallets[addr]["last_faucet"] = now

    return jsonify({
        "success": True,
        "balance": wallets[addr]["balance"]
    })

# =========================
# GET WALLET INFO
# =========================
@app.route("/wallet/<addr>")
def wallet(addr):
    if addr in wallets:
        return jsonify(wallets[addr])
    return jsonify({"error": "not found"})

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    print("🚀 Server starting...")
    app.run(host="0.0.0.0", port=5000)
