import telebot
from telebot import types
import datetime
bot = telebot.TeleBot("6081828152:AAGybGxYNV8RMQBwBTqZ9akyAUQDAS1IJHU") #ключ бота


@bot.message_handler(commands = ['start']) #декоратор при вооде новых команд

# def start(message): # что произойдет при нажатии кнопки start пользователем
#     #bot.send_message(message.chat.id, 'type your first and second name') #1) куда отправляем, 2) что отправляем
#     bot.send_message(message.chat.id, "/button\n/start") #добавим клавиатуру
#     bot.register_next_step_handler(message, sentence) #сбор ответа пользователя.
#     #Первый аргумент - это сообщение пользователя. второй аргумент - функция, которая потом запустится

# @bot.message_handlers(commands = ["button"]) #для обработки новых команд

def start(message): # что произойдет при нажатии кнопки start пользователем
    #bot.send_message(message.chat.id, 'type your first and second name') #1) куда отправляем, 2) что отправляем
    bot.send_message(message.chat.id, '/button') #доб`авим клавиатуру
    #bot.register_next_step_handler(message, sentence) #сбор ответа пользователя.
    #Первый аргумент - это сообщение пользователя. второй аргумент - функция, которая потом запустится

@bot.message_handler(commands = ['button']) #для обработки новых команд
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Make a proposal")
    but2 = types.KeyboardButton("Time now")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "choose bellow", reply_markup=markup)

        
@bot.message_handler(content_types=['text']) #для обработки новых команд
def controller(message):
    print(message.text)
    if message.text == "Make a proposal":
        bot.send_message(message.chat.id, "enter name and surname")
        bot.register_next_step_handler(message, sentence)
    elif message.text == 'Time now':
        bot.send_message(message.chat.id, f"Time now is {datetime.datetime.now()}")
        button(message)


def sentence(message):
    text = message.text
    name = text.split()[0]
    surname = text.split()[1]
    bot.send_message(message.chat.id, f"Your name is {name}. Your surname is {surname}")
    button(message)

bot.infinity_polling() #бесконечная проверка того, что отправил пользователь