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


'''
This function tests whether a player will pass go after their role.

@param position_on board - An array indicating where each player is on the board
@param i - An integer that represents which player is being assessed 
@param spaces_to_move - An integer that indicates how many spaces to move from the players dice roll
@return - boolean 

'''
def passed_go(position_on_board, i, spaces_to_move):
	future_position = (position_on_board[i] + spaces_to_move) % 40
	if position_on_board[i] > future_position:
		return True
	else:
		return False


'''
This function tests if the current tile is currently owned.  This included being owned by the current player.

@param position_on board - An array indicating where each player is on the board
@param i - An integer that represents which player is being assessed 
@return - boolean 

'''
def has_been_purchased(position_on_board, i):
	for players_properties in range(len(owned_properties)):
		if dictionary[position_on_board[i]][0] in owned_properties[players_properties]:
			return True
	return False


'''
This function tests whether the current player owes rent to another player for being on their property

@param position_on board - An array indicating where each player is on the board
@param i - An integer that represents which player is being assessed 
@return - boolean 

'''
def owes_rent(position_on_board, i):
	for players_properties in range(len(owned_properties)):
		if players_properties == i:
			continue
		elif dictionary[position_on_board[i]][0] in owned_properties[players_properties]:
			return True
	return False 


def assess(position_on_board, i):
	if dictionary[position_on_board[i]][1] != None:
		if owes_rent(position_on_board, i):
			player_balances[i] -= dictionary[position_on_board[i]][2]
		elif has_been_purchased(position_on_board, i):
			return
		elif player_balances[i] > dictionary[position_on_board[i]][1] and not owes_rent(position_on_board, i):
			player_balances[i] -= dictionary[position_on_board[i]][1]
			owned_properties[i].append(dictionary[position_on_board[i]][0])


def move(position_on_board, i, spaces_to_move):
	square_counts[(position_on_board[i] + spaces_to_move) % 40] += 1
	if passed_go(position_on_board, i, spaces_to_move):
		player_balances[i] += 200
	position_on_board[i] = (position_on_board[i] + spaces_to_move) % 40
	assess(position_on_board, i)

	
def roll(players, position_on_board):
	num_doubles = 0
	i = 0
	while (i != len(players) or roll_again):
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


lst = list(range(0,40))
players = ['Connor', 'Ashlyn', 'Jack', 'Alexa']
position_on_board = [0, 0, 0, 0]
player_balances = [1500, 1500, 1500, 1500]
square_counts = [0] * 40
owned_properties = [ [], [], [], [] ]


dictionary, chance, community_chest = methods.create_board()
chance_deck, community_chest_deck = methods.shuffle_decks(chance, community_chest)

k = 0
while (k != 1):
	roll(players, position_on_board)
	for i in range(len(player_balances)):
		print(str(players[i]) + ": " + "$" + str(player_balances[i]) + " " + str(owned_properties[i]))
	k += 1


#for i in range(len(player_balances)):
#	print(str(players[i]) + ": " + str(player_balances[i]) + str(owned_properties[i]))

#for i in range(0, len(square_counts)):
#	print(str(i) + ": " + str(square_counts[i]))



