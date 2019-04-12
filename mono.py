from random import randint
import numpy as np
import methods

# This is the initial UI in order to play monopoly
#num_players = int(input("How many people are playing? "))
#players = []
#while (num_players < 2 or num_players > 8):
#	num_players = int(input("Sorry you have input an incorrect value please enter a number between 2 and 8. "))

#for i in range(0, num_players):
#	player_name = input("What would you like to be called player " + str(i+1) + "? " + ": ")
#	players.append(player_name)



def assess(position_on_board, i):
	no_rent = True;
	#print(dictionary[position_on_board[i]][0])
	if dictionary[position_on_board[i]][1] != None:
		for j in range(len(owned_properties)):
			if i == j:
				continue
			elif dictionary[position_on_board[i]][0] in owned_properties[j]:
				player_balances[i] -= dictionary[position_on_board[i]][2]
				no_rent = False;
			else:
				continue
		if player_balances[i] > dictionary[position_on_board[i]][1] and no_rent:
			player_balances[i] -= dictionary[position_on_board[i]][1]
			owned_properties[i].append(dictionary[position_on_board[i]][0])



def move(position_on_board, i, spaces_to_move):
	square_counts[(position_on_board[i] + spaces_to_move) % 40] += 1
	position_on_board[i] = (position_on_board[i] + spaces_to_move) % 40
	assess(position_on_board, i)

	

def roll(players, position_on_board):
	num_doubles = 0
	i = 0
	while ((i != len(players) or roll_again) and player_balances[i] >= 0):
		print(str(players[i]) + " is rolling!")
		roll_again = False
		first_die = randint(1,6)
		second_die = randint(1,6)
		print("They rolled a " + str(first_die) +" and a " + str(second_die))
		if first_die == second_die:
			print("doubles!")
			move(position_on_board, i, first_die+second_die)
			print("you are at position " + str(position_on_board[i]))
			roll_again = True
			num_doubles += 1
			if num_doubles == 3:
				print(str(players[i]) + "GO TO JAIL!")
				position_on_board[i] = 10
				square_counts[10] += 1
		else:
			move(position_on_board, i, first_die+second_die)
			print("you are at position " + str(position_on_board[i]))
			num_doubles = 0
			i += 1

	for j in range(len(position_on_board)):
		print(position_on_board[j])
		print(dictionary[position_on_board[j]])






lst = list(range(0,40))
players = ['Connor', 'Ashlyn', 'Jack', 'Alexa']
position_on_board = [0, 0, 0, 0]
player_balances = [1500, 1500, 1500, 1500]
square_counts = [0] * 40
owned_properties = [ [], [], [], [] ]


dictionary = methods.create_board()
still_players = True
k = 0
while (still_players or k < 5):
	count = 0
	for i in range(len(player_balances)):
		if player_balances[i] < 0:
			count += 1
	if count == 3:
		still_players = False
		break 
	roll(players, position_on_board)
	k += 1



for i in range(len(player_balances)):
	print(str(players[i]) + ": " + str(player_balances[i]) + str(owned_properties[i]))

#for i in range(0, len(square_counts)):
#	print(str(i) + ": " + str(square_counts[i]))




