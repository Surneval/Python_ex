#candys game
# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом,
# вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока,
# который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 

# Determine who is the first player
import random
current_player = random.randint(1, 2)
print(f"The first player will be number {current_player}")

def change_player(current_player):
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player
#count candies
total_candies = 221
total_first = 0
total_second = 0
while total_candies > 0:
    if current_player == 1:
        first_player = int(input(f"Player {current_player} How many candies do you want to take from 1 to 28? "))
        total_first += first_player
        total_candies -= first_player
        print(f"Total candies left: {total_candies}")
        if total_candies > 0:
            current_player = change_player(current_player=current_player)
        else:
            continue
    else:
        second_player = int(input(f"Player {current_player} How many candies do you want to take from 1 to 28? "))
        total_second += second_player
        total_candies -= second_player
        print(f"Total candies left: {total_candies}")
        if total_candies > 0:
            current_player = change_player(current_player=current_player)
        else:
            continue
        
print(f"Player-{current_player} you win")    