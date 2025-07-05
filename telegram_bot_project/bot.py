
import os
from telegram.ext import Updater, MessageHandler, Filters

def reply_messages(update, context):
    message = update.message.text.lower()
    if "مرحبا" in message:
        update.message.reply_text("أهلاً وسهلاً! 😊")
    elif "كيفك" in message or "شلونك" in message:
        update.message.reply_text("تمام الحمد لله، وإنت شلونك؟ 😄")
    else:
        update.message.reply_text("ما فهمت عليك، جرب تكتب مرحبا أو كيفك.")

TOKEN = os.getenv("TOKEN")
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, reply_messages))

updater.start_polling()
print("البوت شغال ✅")
updater.idle()
