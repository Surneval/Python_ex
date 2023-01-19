# Создайте программу для игры в ""Крестики-нолики"" - добавила бота
#playing field
maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#maps = [0, 1, 2, 3, 4, 5, 6, 7, 8] positions

#victories
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

#first player
import random
def first_step():
    go_first = random.randint(1, 2)
    return go_first

#round
def round_step(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# check does anybody win
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

#search for defenite combination 
def check_lines(sum_x, sum_0):
    step = ""
    for combin in victories:
        x = 0
        o = 0
        for i in range(3):
            if maps[combin[i]] == "X":
                x += 1
            elif maps[combin[i]] == "0":
                o += 1
        if o == sum_0 and x == sum_x:
            for j in range (3):
                if maps[combin[j]] != "X" and maps[combin[j]] != "0":
                    step = maps[combin[j]]
    return step

# game novigation for AI
def ai_gaming():
    step = ""
    step = check_lines(2, 0)
    if step == "":
        step = check_lines(0, 2)
    if step == "":
        step = check_lines(1, 0)
    if step == "":
        if maps[4] != "X" and maps[4] != "0":
            step = 5
        elif maps[0] != "X" and maps[0] != "0":
            step = 1
        elif maps[2] !="X" and maps[2] != "0":
            step = 3
        elif maps[6] !="X" and maps[6] != "0":
            step = 7
        elif maps[8] !="X" and maps[8] != "0":
            step = 9
        elif maps[1] !="X" and maps[1] != "0":
            step = 2
        elif maps[3] !="X" and maps[3] != "0":
            step = 4
        elif maps[1] !="X" and maps[5] != "0":
            step = 6
        elif maps[7] !="X" and maps[7] != "0":
            step = 8
    return step


# main game
game_round = 1
count = 0
print("Player-1 is bot")
current_player = first_step()
print(f"The first step is for Player-{current_player} > ")
print(f"Game round - {game_round}")
game_over = False
while game_over == False:
    print_maps()
    #if the first step is for bot
    if current_player == 1:
        symbol = "X"
        step = ai_gaming()
        print(f"Player-{current_player} choose position {step}")
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
    

