import telebot

bot = telebot.TeleBot("6780304179:AAFCtmBJ4y6Z4v_6hjblu_2I0aNUaxyROGc")


# KEYBOARD
keyboard_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_markup.add("Add Information")
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Hello friend", reply_markup=keyboard_markup)

@bot.message_handler(func=lambda message: True)
def name(message):
    if message.text == "Add Information":
        msg = bot.send_message(message.chat.id, "Enter your name : ")
        bot.register_next_step_handler(msg, age)
def age(message):
    global name
    name = message.text
    msg = bot.send_message(message.chat.id, "Enter your age : ")
    bot.register_next_step_handler(msg, show)
def show(message):
    global age
    age = message.text
    bot.send_message(message.chat.id, f"your name is : {name}\nyour age is : {age}")

bot.infinity_polling()

