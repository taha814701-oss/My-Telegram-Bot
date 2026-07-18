from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1713259160:AAGxXKBTX9j7Pe31cBMOAmzcLsp70HMwAF8"

def start(update, context):
    update.message.reply_text("سلام! 🤖 من رباتت هستم.")

def echo(update, context):
    update.message.reply_text(f"گفتی: {update.message.text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    print("ربات روشن شد...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()