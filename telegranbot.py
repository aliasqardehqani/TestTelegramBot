import telebot

bot = telebot.TeleBot("6780304179:AAFCtmBJ4y6Z4v_6hjblu_2I0aNUaxyROGc")

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello KOSIANOooo")

bot.infinity_polling()
