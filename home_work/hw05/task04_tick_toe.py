# Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно,
# необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента,
# каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка,
# на которую мы хотим поставить крестик или нолик,
# и проверку на победу (стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

#creating a field

maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#maps = [0, 1, 2, 3, 4, 5, 6, 7, 8] positions

#victiries
victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

#print maps
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8]) 


import random
def first_step():
    go_first = random.randint(1, 2)
    return go_first

def round_step(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def check_victory():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == 'X' and maps[i[2]]== "X":
            win = "X"
        elif maps[i[0]] == "0" and maps[i[1]] == '0' and maps[i[2]]== "0":
            win = "0"
        else:
            win=""
    return win

# main game

current_player = first_step()
game_round = 1
game_over = False
print(f"Round-{game_round}")
print(f"First step for palayer-{current_player}")
count = 0
while game_over == False:
    print_maps()
    if current_player == 1:
        symbol = "X"
        try:
            step = int(input(f"Player-{current_player} it's your turn.\nEnter a number from 1 to 9 > "))
        except (ValueError, TypeError):
            print("Invalid Input!!! Try Again") 
            continue
        if step < 1 or step > 9: 
            print("Invalid Input!!! Try Again") 
            continue
        if maps[int(step)-1] == "X" or maps[int(step)-1] == "0":
            print("Occupied!!! Try Again") 
            continue
             
    else:
        symbol = "0"
        try:
            step = int(input(f"Player-{current_player} it's your turn.\nEnter a numberfrom 1 to 9 > "))
        except (ValueError, TypeError):
            print("Invalid Input!!! Try Again") 
            continue
        if step < 1 or step > 9: 
            print("Invalid Input!!! Try Again") 
            continue
        if maps[int(step)-1] == "X" or maps[int(step)-1] == "0":
            print("Occupied!!! Try Again") 
            continue
        
    round_step(step, symbol)
    count += 1
    win = check_victory()
    if win != "":
        game_over = True
        print(f"Player-{current_player} win")
    elif win == "" and count >= 9:
        game_over = True
        print("Nobody wins. Game over")
    else:
        game_over = False
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1