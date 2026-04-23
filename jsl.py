import os
os.environ["TZ"] = "UTC"

import time
import threading
import requests
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8616432637:AAF5j4AT2vtD7iGSzVujhkrhc53YSaJMjTc"

# =========================
# DATA USER
# =========================
user_city = {}
user_ids = set()
user_reminder = {}

# =========================
# LOG USER
# =========================
def log_user(update, city="unknown"):
    user = update.effective_user
    print(f"👤 {user.id} | @{user.username} | {city} | {datetime.now()}")

# =========================
# SHOLAT API
# =========================
def get_sholat(city):
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Indonesia&method=2"
    return requests.get(url).json()["data"]["timings"]

# =========================
# KIRIM ADZAN
# =========================
def send_adzan(app, uid, city, name):
    try:
        app.create_task(
            app.bot.send_audio(
                chat_id=uid,
                audio=open("azan.mp3", "rb"),
                caption=f"🕌 Waktu Sholat {name} di {city}"
            )
        )
    except:
        app.create_task(
            app.bot.send_message(
                chat_id=uid,
                text=f"🕌 Waktu Sholat {name} di {city}"
            )
        )

# =========================
# MENU
# =========================
def menu():
    return ReplyKeyboardMarkup(
        [
            ["🕌 Jadwal Sholat"],
            ["📍 Set Kota"],
            ["🎧 Adzan Test"],
            ["🔔 Aktifkan Reminder"],
            ["🔕 Matikan Reminder"],
            ["📊 Info Bot"]
        ],
        resize_keyboard=True
    )

# =========================
# START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_chat.id

    user_ids.add(uid)
    user_city.setdefault(uid, "jakarta")
    user_reminder.setdefault(uid, True)

    log_user(update, user_city[uid])

    await update.message.reply_text(
        "🕌 SHOLAT BOT AKTIF",
        reply_markup=menu()
    )

# =========================
# HANDLE MESSAGE
# =========================
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_chat.id
    text = update.message.text.lower()

    city = user_city.get(uid, "jakarta")

    log_user(update, city)

    if text == "🕌 jadwal sholat":
        data = get_sholat(city)

        await update.message.reply_text(
            f"""🕌 JADWAL SHOLAT ({city})

Subuh : {data['Fajr']}
Dzuhur: {data['Dhuhr']}
Ashar : {data['Asr']}
Maghrib: {data['Maghrib']}
Isya  : {data['Isha']}"""
        )

    elif text == "📍 set kota":
        await update.message.reply_text("Ketik nama kota kamu")

    elif text == "🎧 adzan test":
        send_adzan(context.application, uid, city, "TEST")

    elif text == "🔔 aktifkan reminder":
        user_reminder[uid] = True
        await update.message.reply_text("✔ Reminder ON")

    elif text == "🔕 matikan reminder":
        user_reminder[uid] = False
        await update.message.reply_text("❌ Reminder OFF")

    elif text == "📊 info bot":
        await update.message.reply_text(f"👤 User: {len(user_ids)}")

    else:
        user_city[uid] = text
        await update.message.reply_text(f"✔ Kota diset: {text}")

# =========================
# REMINDER LOOP (NO ASYNC ERROR)
# =========================
def reminder_loop(app):
    while True:
        now = datetime.now().strftime("%H:%M")

        for uid in list(user_ids):
            if not user_reminder.get(uid, True):
                continue

            city = user_city.get(uid, "jakarta")

            try:
                data = get_sholat(city)

                for name, t in data.items():
                    if t.startswith(now):
                        send_adzan(app, uid, city, name)
            except:
                pass

        time.sleep(60)

# =========================
# MAIN
# =========================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🕌 BOT RUNNING STABLE...")

# THREAD REMINDER (ANTI ERROR)
threading.Thread(target=reminder_loop, args=(app,), daemon=True).start()

# RUN BOT NORMAL
app.run_polling()
