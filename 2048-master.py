from telegram import __version__ as tg_version
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7755000535:AAGpGg3WkWefTDe102p3OEXbJV4nb6BeD3s"
GAME_URL = "https://danilreznickyi.github.io/2048-master/"  # Link to your game

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = (
        "Welcome to 2048-Master 🎮\n\n"
        "Press the button below to launch the game directly in Telegram!"
    )
    # Check Telegram library version
    if tg_version < "20.0":
        await context.bot.send_message(chat_id=chat_id, text="Please update the library!")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                text="Launch 2048", web_app={"url": GAME_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
