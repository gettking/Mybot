from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8616432637:AAF5j4AT2vtD7iGSzVujhkrhc53YSaJMjTc"

URL = "https://USERNAME.github.io/repo/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 PLAY GAME", web_app={"url": URL})]
    ]

    await update.message.reply_text(
        "Klik untuk main game 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("BOT RUNNING...")
app.run_polling()
