# the same candies game with bot
# bot always win if it goes first
# if bot is not starting it can't win only if the second player plays wisely: firstly to take a reminder
# and then total sum of candies should be 29
# if the second players has no strategy, bot also wins
import random
go_first = random.randint(1, 2)
current_player = go_first
print(f"Player-1 is bot")
print(f"The first player will be Player-{current_player}")


def change_player(current_player):
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player


# count candies
max_candies = 28
total_candies = 221
total_first = 0
total_second = 0
first_player = 0
second_player = 0
remainder = 221 % (max_candies + 1)
step = 1
print(f"Round-{step}")

while total_candies > 0:
    if go_first == 1:
        while step < 2:
            first_player = total_candies % (max_candies+1)
            print(f"Player-{current_player} took {first_player} candies")
            total_first += first_player
            total_candies -= first_player
            step += 1
            print(f"Total candies left: {total_candies}")
            print(f"The next round-{step}")
            if total_candies > 0:
                current_player = change_player(current_player=current_player)
            else:
                continue
        if current_player == 1:
            first_player = max_candies + 1 - second_player
            print(f"Player-{current_player} took {first_player} candies")
            total_first += first_player
            total_candies -= first_player
            step += 1
            print(f"Total candies left: {total_candies}")
            print(f"The next round-{step}")
            if total_candies > 0:
                current_player = change_player(current_player=current_player)
            else:
                continue
        else:
            second_player = int(input(
                f"Player {current_player} How many candies do you want to take from 1 to 28? "))
            total_second += second_player
            total_candies -= second_player
            step += 1
            print(f"Total candies left: {total_candies}")
            print(f"The next round-{step}")
            if total_candies > 0:
                current_player = change_player(current_player=current_player)
            else:
                continue

    else:
        if current_player == 2:
            second_player = int(input(
                f"Player {current_player} How many candies do you want to take from 1 to 28? "))
            total_second += second_player
            total_candies -= second_player
            step += 1
            print(f"Total candies left: {total_candies}")
            print(f"The next round-{step}")
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
                remainder -= num
                total_first += first_player
                total_candies -= first_player
                step += 1
                print(f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
            else:
                first_player = max_candies + 1 - second_player
                print(f"Player-{current_player} took {first_player} candies")
                remainder -= num
                total_first += first_player
                total_candies -= first_player
                step += 1
                print(f"Total candies left: {total_candies}")
                print(f"The next round-{step}")
            if total_candies > 0:
                current_player = change_player(current_player=current_player)
            else:
                continue
print(f"Player-{current_player} you win")
if current_player == 1:
    print(
        f"Player-{current_player} you receive {total_second} candies from the second player")
else:
    print(
        f"Player-{current_player} you receive {total_first} candies from the first player")
