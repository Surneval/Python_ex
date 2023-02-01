import telebot
from telebot import types



bot = telebot.TeleBot("5994903484:AAG21HZ3ipztIHnx6tRF38WQZO6ngqUDZeU")
result = 0
numbs = (0, 0)
operation = ""
calc_mode = ""

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("real numbers")
    but2 = types.KeyboardButton("complex numbers")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "choose bellow", reply_markup=markup)
    bot.register_next_step_handler(message, calculations)

@bot.message_handler(content_types=['text'])
def calculations(message):
    global calc_mode
    calc_mode = message.text
    if calc_mode == 'real numbers':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but2 = types.KeyboardButton("+")
        but3 = types.KeyboardButton("-")
        but4 = types.KeyboardButton("/")
        but5 = types.KeyboardButton("*")
        but6 = types.KeyboardButton("**")
        but7 = types.KeyboardButton("%")
        but8 = types.KeyboardButton("//")
        markup.add(but2)
        markup.add(but3)
        markup.add(but4)
        markup.add(but5)
        markup.add(but6)
        markup.add(but7)
        markup.add(but8)

        bot.send_message(message.chat.id, "Choose an operation", reply_markup=markup)
        bot.register_next_step_handler(message,operation_input)

    elif calc_mode == 'complex numbers':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but2 = types.KeyboardButton("+")
        but3 = types.KeyboardButton("-")
        but4 = types.KeyboardButton("/")
        but5 = types.KeyboardButton("*")
        but6 = types.KeyboardButton("**")
        
        markup.add(but2)
        markup.add(but3)
        markup.add(but4)
        markup.add(but5)
        markup.add(but6)

        bot.send_message(message.chat.id, "Choose an operation", reply_markup=markup)
        bot.register_next_step_handler(message, operation_input)

def user_input(message):
    global numbs
    if calc_mode == 'real numbers':
        try:
            number_1 = int(message.text.split()[0])
            number_2 = int(message.text.split()[1])
        except(ValueError, TypeError):
            bot.send_message(message.chat.id, "Mistake. Enter two numbers 'number_x number_y' with a 'space' between")
    elif calc_mode == 'complex numbers': 
            try:
                number_1 = complex(message.text.split()[0])
                number_2 = complex(message.text.split()[1])
            except(ValueError, TypeError):
                bot.send_message(message.chat.id, "Mistake. Enter two numbers 'number_x number_y' with a 'space' between")
    numbs = (number_1, number_2)
    controller(message)

def operation_input(message):
    global operation
    operation = message.text
    get_numbers(message)

def controller(message):
    global operation
    global numbs
    global result
    
    if operation == "+":
        result = numbs[0] + numbs [1]
    elif operation == '-':
        result = numbs[0] - numbs[1]
    elif operation == "*":
        result = numbs[0] * numbs[1]
    elif operation == "/":
        result = numbs[0] / numbs[1]
    elif operation == "//":
        result = numbs[0] // numbs[1]
    elif operation == "%":
        result = numbs[0] % numbs[1]
    elif operation == "**":
        result = numbs[0] ** numbs[1]
    bot.send_message(message.chat.id, f"{numbs[0]} {operation} {numbs[1]} = {result}")
    bot.send_message(message.chat.id, f"Press /start for main menu")


def get_numbers(message):
    if calc_mode == 'real numbers':
        bot.send_message(message.chat.id, "Enter 2 real numbers separated by space. Ex: '12 15'")
        bot.register_next_step_handler(message,user_input)
    elif calc_mode == 'complex numbers':
        bot.send_message(message.chat.id, "Enter 2 complex numbers separated by space. Ex: '1+5j 2+6j'")
        bot.register_next_step_handler(message,user_input)
    

bot.infinity_polling() #бесконечная проверка того, что отправил пользователь 