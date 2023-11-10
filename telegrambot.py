import telebot

bot = telebot.TeleBot("Telegram Bot Token")

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello KOSIANOooo")


@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you help?")


bot.infinity_polling()
