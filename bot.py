from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8616432637:AAF5j4AT2vtD7iGSzVujhkrhc53YSaJMjTc"

GAME_URL = "https://username.github.io/repo/"

# =========================
# START COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 Play L1 TEST TO MAIN",
                web_app=WebAppInfo(url=GAME_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🧪 Welcome to L1 TEST TO MAIN\nKlik tombol di bawah untuk masuk game 👇",
        reply_markup=reply_markup
    )

# =========================
# RUN BOT
# =========================
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot running...")
app.run_polling()
