import telebot
bot = telebot.TeleBot("6780304179:AAFCtmBJ4y6Z4v_6hjblu_2I0aNUaxyROGc")


# Add inline button to bot for join channel or group or anything
button = telebot.types.InlineKeyboardButton("CheckThis", url="https://t.me/+F8mHTtgn-t0yM2Jk")
mark_up = telebot.types.InlineKeyboardMarkup()
mark_up.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello Debugger", reply_markup=mark_up)  # This is send message when you /start the bot


@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you help?")  # When you have need help click /help in BOT


bot.infinity_polling()
