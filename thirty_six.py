# let us c
# Write a program for a match-stick game between the computer and a user. your program
# should ensure that the computer always wins. Rules for the game are as follows:
# - There are 21 match-sticks.
# - The computer asks the player to pick 1, 2, 3, or 4 match sticks.
# - After the person picks, the computer does its picking.
# - Whoever is forced to pick up the last match-stick loses the game.
def match_stick_game(arr, a):
    for i in range(a):
        print(5 - arr[i], end=" ")


arr = [1, 6, 3, 2]

a = len(arr)

match_stick_game(arr, a)
