import telebot
bot = telebot.TeleBot("")


# Add inline button to bot for join channel or group or anything
button = telebot.types.InlineKeyboardButton("Error Channel", url="https://t.me/+F8mHTtgn-t0yM2Jk")
mark_up = telebot.types.InlineKeyboardMarkup()
mark_up.add(button)

# Add Keyboard button to Bot
keyboard_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_markup.add("parts", "send ticket", 'operator')

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello Debugger", reply_markup=mark_up)  # This is send message when you /start the bot


@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you help?", reply_markup=keyboard_markup)  # When you have need help click /help in BOT

op = "https://t.me/aliasqardehqani"
@bot.message_handler()
def keyboard(message):
    if message.text == "parts":
        bot.send_message(message.chat.id, "You can use new username")
    elif message.text == "send ticket":
        bot.send_message(message.chat.id, "Please write your ticket : ")
    elif message.text == "operator":
        bot.send_message(message.chat.id, f"send message to {op}")

bot.infinity_polling()
