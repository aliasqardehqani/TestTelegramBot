import telebot

bot = telebot.TeleBot("Telegram Bot Token")

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello KOSIANOooo")  # This is send message when you /start the bot


@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you help?")  # When you have need help click /help in BOT


bot.infinity_polling()
