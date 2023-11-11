import telebot
import regex
import re
bot = telebot.TeleBot("6780304179:AAFCtmBJ4y6Z4v_6hjblu_2I0aNUaxyROGc")

# Add inline button to bot for joining a channel or group or anything
button = telebot.types.InlineKeyboardButton("Error Channel", url="https://t.me/+F8mHTtgn-t0yM2Jk")
callback_button = telebot.types.InlineKeyboardButton("button", callback_data="Hi")
testbutton = telebot.types.InlineKeyboardButton("testbutton", callback_data="Hallo")
mark_up = telebot.types.InlineKeyboardMarkup()
mark_up.add(button, callback_button)

# Add Keyboard button to Bot
keyboard_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_markup.add("parts", "send ticket", 'operator')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.send_message(call.message.chat.id, "You clicked on a button")  # show a pm
    bot.answer_callback_query(call.id, "شما کلیک کردی؟ :)")  # show a notification
    bot.answer_callback_query(call.id, "شما کلیک کردی؟ :)", show_alert=True)  # show a Alert Notification

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello Debugger", reply_markup=mark_up)

@bot.message_handler(commands=['help'])
def reply_message(message):
    bot.reply_to(message, "What do you need help with?", reply_markup=keyboard_markup)

op = "https://t.me/aliasqardehqani"

@bot.message_handler(func=lambda message: True)  # This is to mean bot receive all of message from user : func=lambda message: True
def handle_messages(message):
    if message.text == "parts":
        bot.send_message(message.chat.id, "You can use a new username.")
    elif message.text == "send ticket":
        bot.send_message(message.chat.id, "Please write your ticket:")
    elif message.text == "operator":
        bot.send_message(message.chat.id, f"Send a message to {op}")

@bot.message_handler(commands=['cancel', 'help'])
def message_handler(message):
    bot.send_message(message.chat.id, "این یک دستور ارسال شده است")

@bot.message_handler(func=lambda m: m.text == "testbutton")
def button(message):
    print(message.chat.type)
    print(message.chat.id)
    print(message.chat.username)
    bot.send_message(message.chat.id, "you click the (testbutton)")


# @bot.message_handler(func=lambda message: re.search(r'\d+', message.text))
# def check_number(message):
#     bot.send_message(message.chat.id, "You entered a number in your text")

@bot.message_handler(chat_types=['private'])
def check_pv(message):
    print(message.chat.type)
    print(message.chat.id)
    print(message.chat.username)
    bot.send_message(message.chat.id, "You send message from pv")


@bot.message_handler(chat_types=['group'])
def check_group(message):
    print(message.chat.type)
    print(message.chat.id)
    print(message.chat.username)
    bot.send_message(message.chat.id, "You send message from group")

bot.infinity_polling()
