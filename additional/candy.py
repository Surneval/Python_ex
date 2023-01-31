import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot("6197246160:AAEd0x5ojhbV8iSMhub1N_t1Uza3SIH8Q_Q") #ключ бота. Инициация класса

@bot.message_handler(commands = ['start']) #декоратор при вводе новых команд. Старт бота

def start(message):
    bot.send_message(message.chat.id, 'Enter your name and surname')
    bot.register_next_step_handler(message, sentence)
    

@bot.message_handler(content_types=['text'])
def sentence(message):
    text = message.text
    name = text.split()[0]
    surname = text.split()[1]
    bot.send_message(message.chat.id, f"Hello {name} {surname}. Let's play a game :)")
    bot.send_message(message.chat.id, '/game')
    bot.register_next_step_handler(message, game)
    
@bot.message_handler(commands = ['game'])
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Start a game")
    markup.add(but1)
    bot.send_message(message.chat.id, "choose bellow", reply_markup=markup)
    bot.register_next_step_handler(message, start_game)
    

@bot.message_handler(content_types=['text'])
def start_game(message):
    print(message.text)
    if message.text == "Start a game":
        bot.send_message(message.chat.id, "We have 221 candies.\nWe will take from 1 to 28 candies at a time\nTre player who makes the last move wins\nNow let's randomly choose the first player.") 
        bot.register_next_step_handler(message, main_game)
        
    
@bot.message_handler(content_types=['text'])   
def main_game(message):
    #choose who plays first
    #global second_player
    #global second_player, go_fist, current_player, max_candies, total_candies, total_first, total_second, first_player
    go_first = random.randint(1, 2)
    bot.send_message(message.chat.id, f'Player-1 is me - bot. Player-2 is you. The first player will be Player-{go_first}')
    current_player = go_first
    max_candies = 28
    total_candies = 221
    total_first = 0
    total_second = 0
    first_player = 0
    second_player = 0
    remainder = 221 % (max_candies + 1)
    step = 1
    print(f"Round-{step}")
    bot.send_message(message.chat.id, f"Round-{step}")
        
    while total_candies > 0:
        if go_first == 1:
            while step < 2:
                first_player = total_candies % (max_candies+1)
                print(f"Player-{current_player} took {first_player} candies")
                bot.send_message(message.chat.id, f"Player-{current_player} took {first_player} candies")
                total_first += first_player
                total_candies -= first_player
                step += 1
                print(f"Total candies left: {total_candies}")
                bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
                bot.send_message(message.chat.id, f"The next round-{step}")
                if total_candies > 0:
                    current_player = change_player(current_player=current_player)
                else:
                    continue
            if current_player == 1:
                first_player = max_candies + 1 - second_player
                print(f"Player-{current_player} took {first_player} candies")
                bot.send_message(message.chat.id, f"Player-{current_player} took {first_player} candies")
                total_first += first_player
                total_candies -= first_player
                step += 1
                print(f"Total candies left: {total_candies}")
                bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
                bot.send_message(message.chat.id, f"The next round-{step}")
                if total_candies > 0:
                    current_player = change_player(current_player=current_player)
                else:
                    continue
            else:
                bot.send_message(message.chat.id, f"Player-{current_player} it's you turn. How many candies will you take?")
                time.sleep(5)
                bot.register_next_step_handler(message, get_number)

                second_player = get_number(message)
                total_second += second_player
                total_candies -= second_player
                step += 1
                print(f"Total candies left: {total_candies}")
                bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
                bot.send_message(message.chat.id, f"The next round-{step}")
                if total_candies > 0:

                    current_player = change_player(current_player=current_player)
                else:
                    continue

        else:
            if current_player == 2:
                bot.send_message(message.chat.id, f"Player-{current_player} it's you turn. How many candies will you take?")
                time.sleep(5)
                bot.register_next_step_handler(message, get_number)
                
                
                second_player = get_number(message)
                total_second += second_player
                total_candies -= second_player
                step += 1
                print(f"Total candies left: {total_candies}")
                bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
                bot.send_message(message.chat.id, f"The next round-{step}")
                if total_candies > 0:
                    current_player = change_player(current_player=current_player)
                else:
                    continue
            else:
                if remainder > 0:
                    num = max_candies - (max_candies + 1 - second_player)
                    first_player = (max_candies + 1 - second_player) + \
                        min(remainder, num)
                    print(f"Player-{current_player} took {first_player} candies")
                    bot.send_message(message.chat.id, f"Player-{current_player} took {first_player} candies")
                    remainder -= num
                    total_first += first_player
                    total_candies -= first_player
                    step += 1
                    print(f"Total candies left: {total_candies}")
                    bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                    print(f"The next round-{step}")
                    bot.send_message(message.chat.id, f"The next round-{step}")
                else:
                    first_player = max_candies + 1 - second_player
                    print(f"Player-{current_player} took {first_player} candies")
                    bot.send_message(message.chat.id, f"Player-{current_player} took {first_player} candies")
                    remainder -= num
                    total_first += first_player
                    total_candies -= first_player
                    step += 1
                    print(f"Total candies left: {total_candies}")
                    bot.send_message(message.chat.id, f"Total candies left: {total_candies}")
                    print(f"The next round-{step}")
                    bot.send_message(message.chat.id, f"The next round-{step}")
                if total_candies > 0:
                    current_player = change_player(current_player=current_player)
                else:
                    continue
    print(f"Player-{current_player} you win")
    bot.send_message(message.chat.id, f"Player-{current_player} you win")
    if current_player == 1:
        print(
            f"Player-{current_player} you receive {total_second} candies from the second player")
        bot.send_message(message.chat.id, f"Player-{current_player} you receive {total_second} candies from the second player")
    else:
        print(
            f"Player-{current_player} you receive {total_first} candies from the first player")
        bot.send_message(message.chat.id, f"Player-{current_player} you receive {total_first} candies from the first player")

def change_player(current_player):
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player

def get_number(message):
    #global second_player
    text = message.text
    second_player = int(text)
    return second_player

bot.infinity_polling() #бесконечная проверка того, что отправил пользователь
