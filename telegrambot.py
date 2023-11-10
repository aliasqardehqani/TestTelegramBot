import telebot

bot = telebot.TeleBot("6780304179:AAFCtmBJ4y6Z4v_6hjblu_2I0aNUaxyROGc")

# Add inline button to bot for joining a channel or group or anything
button = telebot.types.InlineKeyboardButton("Error Channel", url="https://t.me/+F8mHTtgn-t0yM2Jk")
callback_button = telebot.types.InlineKeyboardButton("button", callback_data="Hi")
mark_up = telebot.types.InlineKeyboardMarkup()
mark_up.add(button, callback_button)

# Add Keyboard button to Bot
keyboard_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_markup.add("parts", "send ticket", 'operator')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.send_message(call.message.chat.id, "You clicked on a button")

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello Debugger", reply_markup=mark_up)

@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you need help with?", reply_markup=keyboard_markup)

op = "https://t.me/aliasqardehqani"
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "parts":
        bot.send_message(message.chat.id, "You can use a new username.")
    elif message.text == "send ticket":
        bot.send_message(message.chat.id, "Please write your ticket:")
    elif message.text == "operator":
        bot.send_message(message.chat.id, f"Send a message to {op}")

bot.infinity_polling()
