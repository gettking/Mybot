wallets = {}

import random, string

def gen_address():
    return "TTM" + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# =========================
# CREATE WALLET
# =========================
@app.route("/create_wallet", methods=["POST"])
def create_wallet():
    data = request.json

    addr = gen_address()

    wallets[addr] = {
        "username": data["username"],
        "password": data["password"],
        "balance": 0,
        "history": []
    }

    return jsonify({
        "address": addr
    })

# =========================
# GET WALLET INFO
# =========================
@app.route("/wallet/<addr>")
def wallet(addr):

    if addr not in wallets:
        return jsonify({"error": "wallet not found"})

    return jsonify(wallets[addr])
