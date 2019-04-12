import random

def create_board():
	board = {
	0 : ("GO!", None, None),
	1 : ("Mediterranean Avenue", 60, 2),
	2 : ("Community Chest", None, None),
	3 : ("Baltic Avenue", 60, 3),
	4 : ("Income Tax", None, -200),
	5 : ("Reading Railroad", 200, 25),
	6 : ("Oriental Avenue", 100, 6),
	7 : ("Chance", None, None),
	8 : ("Vermont Avenue", 100, 6),
	9 : ("Connecticut Avenue", 120, 8),
	10 : ("JAIL", None, None),
	11 : ("St. Charles Place", 140, 10),
	12 : ("Electric Company", 150, 0),
	13 : ("States Avenue", 140, 10),
	14 : ("Virginia Avenue", 160, 12),
	15 : ("Pennsylvania Railroad", 200, 25),
	16 : ("St. James Place", 180, 14),
	17 : ("Community Chest", None, None),
	18 : ("Tennessee Avenue", 180, 14),
	19 : ("New York Avenue", 200, 16),
	20 : ("Free Parking", None, None),
	21 : ("Kentucky Avenue", 220, 18),
	22 : ("Chance", None, None),
	23 : ("Indiana Avenue", 220, 18),
 	24 : ("Illinois Avenue", 240, 20),
 	25 : ("B&O Railroad", 200, 25),
 	26 : ("Atlantic Avenue", 260, 22),
 	27 : ("Ventnor Avenue", 260, 22),
 	28 : ("Water Works", 150, 0),
 	29 : ("Marvin Gardens", 280, 24),
 	30 : ("GO TO JAIL!", None, None),
 	31 : ("Pacific Avenue", 300, 26),
 	32 : ("North Carolina Avenue", 300, 26),
 	33 : ("Community Chest", None, None),
 	34 : ("Pennsylvania Avenue", 320, 28),
 	35 : ("Short Line", 200, 25),
 	36 : ("Chance", None, None),
 	37 : ("Park Place", 350, 35),
 	38 : ("Luxury Tax", None, -75),
 	39 : ("Boardwalk", 400, 50)
	}

	chance = {
	0 : ("Advance to Go (Collect $200)", 0, 200),
	1 : ("Advance to Illinois Avenue. If you pass GO collect $200!", 24, None),
	2 : ("Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.", "12/28", "150/roll"),
	3 : ("Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", "5/15/25/35", "200/2_times_rent"),
	4 : ("Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", "5/15/25/35", "200/2_times_rent"),
	5 : ("Bank pays you dividend of $50", None, 50),
	6 : ("Get out of Jail Free. This card may be kept until needed, or traded/sold", None, None),
	7 : ("Go Back Three 3 Spaces.", 3, None),
	8 : ("Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.", 10, None),
	9 : ("Make general repairs on all your property: For each house pay $25, For each hotel pay $100.", None, "25/100"),
	10 : ("Pay poor tax of $15.", None, 15),
	11 : ("Take a trip to Reading Railroad. If you pass Go, collect $200.", 5, 200),
	12 : ("Take a walk on the Boardwalk. Advance token to Boardwalk.", 39, None),
	13 : ("You have been elected Chairman of the Board. Pay each player $50.", None, -50),
	14 : ("Your building and loan matures. Receive Collect $150.", None, 150),
	15 : ("You have won a crossword competition—Collect $100", None, 100),
	16 : ("Advance to St. Charles Place – If you pass Go, collect $200", 11, None)

	}

	community_chest = {
	0 : ("Advance to Go (Collect $200)", 0, 200),
	1 : ("Bank error in your favor. Collect $200.", None, 200),
	2 : ("Doctor's fees. Pay $50.", None, -50),
	3 : ("Get out of Jail Free. This card may be kept until needed, or traded/sold", None, None),
	4 : ("Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.", 10, None),
	5 : ("Grand Opera Night. Collect $50 from every player for opening night seats.", None, 50),
	6 : ("Holiday Fund matures. Receive $100.", None, 100),
	7 : ("Income tax refund. Collect $20.", None, 20),
	8 : ("It is your birthday. Collect $10 from every player.", None, 10),
	9 : ("Life insurance matures – Collect $100.", None, 100),
	10 : ("Hospital Fees. Pay $50.", None, 50),
	11 : ("School fees. Pay $50.", None, 50),
	12 : ("Receive $25 consultancy fee.", None, 25),
	13 : ("You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.", None, "40/115"),
	14 : ("You have won second prize in a beauty contest. Collect $10.", None, 10),
	15 : ("You inherit $100.", None, 100),
	16 : ("From sale of stock you get $50", None, 50)
	}
	return board, chance, community_chest


def shuffle_decks(chance, community_chest):
	chance_deck = []
	community_chest_deck = []
	for i in range(len(chance)):
		chance_deck.append(chance[i])
		community_chest_deck.append(community_chest[i])
	return random.shuffle(chance_deck), random.shuffle(community_chest_deck)



