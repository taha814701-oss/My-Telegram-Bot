from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن رباتت رو اینجا بذار
TOKEN ="1713259160:AAGxXKBTX9j7Pe31cBMOAmzcLsp70HMwAF8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 🤖 من رباتت هستم.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"گفتی: {update.message.text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("ربات روشن شد...")
app.run_polling()