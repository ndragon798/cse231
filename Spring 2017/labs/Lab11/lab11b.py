
import cards

# Create the deck of cards
def start(decksize):
	the_deck = cards.Deck()
	the_deck.shuffle()


	player1_list=[]
	player2_list=[]
	for i in range( decksize ):
	    player1_list.append( the_deck.deal() )
	    player2_list.append( the_deck.deal() )
	return player1_list,player2_list
def game(player1_list,player2_list):
	try:
		player1_card=player1_list.pop(0)
		player2_card=player2_list.pop(0)
		print("Player 1:",player1_card,"Player 2:",player2_card)
		if player1_card.rank() ==player2_card.rank():
			print("Stalemate")
			player1_list.append(player1_card)
			player2_list.append(player2_card)
		elif player1_card.rank() == 1:
			print("Player 1 has won this round")
			player1_list.append(player1_card)
			player1_list.append(player2_card)
		elif player2_card.rank()==1:
			print("Player 2 has won this round")
			player2_list.append(player1_card)
			player2_list.append(player2_card)
		elif player1_card.rank()>player2_card.rank():
			print("Player 1 has won this round")
			player1_list.append(player1_card)
			player1_list.append(player2_card)
		elif player1_card.rank()<player2_card.rank():
			print("Player 2 has won this round")
			player2_list.append(player1_card)
			player2_list.append(player2_card)
	except:
		if len(player2_list)==0:
			print("Player 1 has won.")
			cont=False
		elif len(player1_list)==0:
			print("Player 2 has won.")
			cont=False
player1_list,player2_list=start(26)
#print(player1_list,player2_list)
cont=True
while cont:
	if len(player1_list)==0:
		print("Player 2 has won.")
		break
	elif len(player2_list)==0:
		print("Player 1 has won.")
		break
	game(player1_list,player2_list)
	#print(player1_list,player2_list)
	acont=input("Continue? Y/N: ")
	if acont.lower()!='n':
		cont=True
	else:
		cont=False
		if len(player1_list)>len(player2_list):
			print("Player 1 has Won.")
		else:
			print("Player 2 has Won.")

	