import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot("6197246160:AAEd0x5ojhbV8iSMhub1N_t1Uza3SIH8Q_Q")

total_candies = 200
max_candies = 28
user_turn = 0
bot_turn = 0
flag = ""
step = 1
go_first = ""
remainder = total_candies % (max_candies + 1)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/rules")
    but2 = types.KeyboardButton("/game")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "choose bellow", reply_markup=markup)

@bot.message_handler(commands = ['rules'])
def rules(message):
    bot.send_message(message.chat.id, 'We have some candies.\nEach player will take from 1 to 28 candies at a time\nThe player who makes the last move wins')

@bot.message_handler(commands=["game"])
def game(message):
    global flag
    bot.send_message(message.chat.id,f"Let's start a game")
    bot.send_message(message.chat.id, f"We have {total_candies} candies left")
    go_first = random.choice(["user", "bot"])
    flag = go_first

    if flag == "user":
        bot.send_message(message.chat.id,f"User plays first")
        controller(message, flag)
    else:
        bot.send_message(message.chat.id, f"Bot plays first")
        controller(message, flag)

def controller(message, flag):
    if total_candies > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Your turn. Enter a number of candies from 0 up to {max_candies}")
            bot.register_next_step_handler(message,user_input)
        else:
            bot.send_message(message.chat.id, f"Now it's bot turn")
            bot_input(message)
    else:
        bot.send_message(message.chat.id, f"{flag} win. Congrats!")


def user_input(message):
    global user_turn
    global step
    global total_candies
    global flag

    try:
        user_turn = int(message.text)
    except(ValueError, TypeError):
        bot.send_message(message.chat.id, "Enter a number please")
    step += 1
    total_candies -= user_turn
    
    if total_candies > 0:
        flag = 'user' if flag == 'bot' else 'bot'
        controller(message, flag)
    else:
        controller(message, flag)
    

def bot_input(message):
    global bot_turn
    global step
    global remainder
    global total_candies
    global flag
    
    if go_first == "bot":
        while step < 2:
            bot_turn = total_candies % (max_candies + 1)
            step += 1
            total_candies -= bot_turn
            bot.send_message(message.chat.id, f"Bot took {bot_turn} candies")
            bot.send_message(message.chat.id, f"We have {total_candies} candies left")

            if total_candies > 0:
                flag = 'user' if flag == 'bot' else 'bot'
                controller(message, flag)
            else:
                controller(message, flag)

        bot_turn = max_candies + 1 - user_turn
        total_candies -= bot_turn
        step += 1

        bot.send_message(message.chat.id, f"Bot took {bot_turn} candies")
        bot.send_message(message.chat.id, f"We have {total_candies} candies left")

        if total_candies > 0:
            flag = 'user' if flag == 'bot' else 'bot'
            controller(message, flag)
        else:
            controller(message, flag)
    else:
        if remainder > 0:
            num = max_candies - (max_candies + 1 - user_turn)
            bot_turn = (max_candies + 1 - user_turn) + min(remainder, num)
            remainder -= num
            total_candies -= bot_turn
            step += 1
            bot.send_message(message.chat.id, f"Bot took {bot_turn} candies")
            bot.send_message(message.chat.id, f"We have {total_candies} candies left")
            if total_candies > 0:
                flag = 'user' if flag == 'bot' else 'bot'
                controller(message, flag)
            else:
                controller(message, flag)
        else:
            bot_turn = max_candies + 1 - user_turn
            total_candies -= bot_turn
            step += 1
            bot.send_message(message.chat.id, f"Bot took {bot_turn} candies")
            bot.send_message(message.chat.id, f"We have {total_candies} candies left")
            if total_candies > 0:
                flag = 'user' if flag == 'bot' else 'bot'
                controller(message, flag)
            else:
                controller(message, flag)

bot.infinity_polling() #бесконечная проверка того, что отправил пользователь    
