import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8710010478:AAHipNvQdTvgsOUDm5ct76mV9O1Tc_zcgu8"

logging.basicConfig(level=logging.INFO)

BAD_WORDS = ["خفه شو", "بی ناموس", "بی شعور", "بد بخت", "بی تربیت"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "سلام" in text:
        reply = "سلام کوچول من داش مرتضی هستم"
    elif "چطوری" in text:
        reply = "من خوبم ولی اگه تو خوب باشی ۲۶ میشی."
    elif "تو کی هستی" in text:
        reply = "من مرتضی هستم."
    elif "تو خیلی خری" in text:
        reply = "الان به برنا میگم بیست و ششت کنه ها!"
    elif "تو از پارمین بدت میاد" in text:
        reply = "من! نه، من از پارمین متنفرم 😤"
    elif any(bad in text for bad in BAD_WORDS):
        reply = "یه بار دیگه بگی ۲۶ میشی. 😤"
    else:
        reply = None
    if reply:
        await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("ربات داره اجرا میشه...")
    app.run_polling()
