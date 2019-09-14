import EgyptionWarHelper as EH


"Explanation of the solution:"
"card1 is the current card to check,card2 is the next card that will be checked"
"You need card2 because "
global storage#so you can access it from all functions

def reset_variables():
    cardsLeft = 0
    storage = []
    return cardsLeft,storage


def continue_game(input):
    while input != ' ':
        input = input('click space to continue')

def turn(nxt):
    if nxt == 'player1':
        card = EH.pull_out_card(player1, nxt)
        nxtTurn = 'player2'
    else:
        card = EH.pull_out_card(player2, nxt)
        nxtTurn = 'player1'
    storage.append(card)
    return nxtTurn,card

def update_deck(nxtTurn,deck1,deck2):
    if nxtTurn == 'player1':
        deck1+=storage
    deck2+=storage

"Royal mode is executing the same code as the progress of the game with 1 diffrence:"
"a different condition for someone to win the storage which is by the cardsLeft(means he didn't place a royal card"
"I created a function for it just so it will be more readable"
def royal_mode(cardsLeft,nxtTurn,card,storage,deck1,deck2):
    player1,player2=deck1,deck2
    card1 = card
    card2 = ''
    if len(deck1)<cardsLeft:
        cardsLeft=len(deck1)

    if EH.check_slaps(storage):  # Slaps
        EH.print_winner(nxtTurn, storage)
        update_deck(nxtTurn,player1,player2)
        cardsLeft,storage = reset_variables()
    elif EH.is_royal(card1):
        nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
        cardsLeft = EH.cards_left(card1)

    while cardsLeft > 0:
        b = input('click space to continue')
        continue_game(b)
        if nxtTurn == 'player1':#its the same player's turn untill he draws a royal card or loses the round.
            card2 = EH.pull_out_card(deck1, nxtTurn)
        else:
            card2 = EH.pull_out_card(deck2, nxtTurn)
        storage.append(card2)
        cardsLeft = cardsLeft - 1
        card1 = card2


        if EH.check_slaps(storage):
            nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'# Slaps
            EH.print_winner(nxtTurn, storage)
            update_deck(nxtTurn,player1,player2)
            cardsLeft,storage = reset_variables()
            break
        elif EH.is_royal(card1):
            nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
            cardsLeft = EH.cards_left(card1)

    if len(storage)!=0:#If the loop was stopped because cardsLeft<0 and not slap(break)
        nxtTurn = 'player2' if nxtTurn == 'player1' else 'player1'
        EH.print_winner(nxtTurn, storage)
        update_deck(nxtTurn,player1,player2)
        return player1,player2,nxtTurn
    return player1, player2, nxtTurn


while True:
    try:
        print('Click space to play a normal game')
        print('Enter the amount(17-26) of cards you want for each player.')
        N = input()
        if N == ' ':
            N = 26
            print(N)
            break
        else:
            N = int(N)
            if N <= 26 and N > 17:#17 because of the chance that both players will get only royals
                break
    except ValueError:
        print('Please enter a number ')
    else:
        print('Please enter a number between 1 and 25 or click space for a standard game')
player1 = []  # player1's deck
player2 = []  # player2's deck
player1, player2 = EH.create_decks(player1, player2, N)
cardsLeft = 0#How many cards does the current player have left to draw out while the other one has drown a royal.
storage = []#Stores the current cards that the winner of the round will get.

nxtTurn = 'player1'#Stores the name of the player that should draw a card next.
card1 = EH.pull_out_card(player1, nxtTurn)#Stores the card that is checked at the current turn
card2=''#stores the card that has been drawn now.(the card that is being printed
nxtTurn = 'player2'
storage.append(card1)

"The progress of the game"
while len(player1)>0 and len(player2)>0:
    b = input('click space to continue')
    continue_game(b)


    nxtTurn,card2=turn(nxtTurn)
    # Normal slaps
    if EH.check_slaps(storage):
        EH.print_winner(nxtTurn, storage)
        update_deck(nxtTurn,player1,player2)
        cardsLeft,storage = reset_variables()
        nxtTurn,card2=turn(nxtTurn)
        card1 = card2
        continue


    if EH.is_royal(card1):#Royals
        cardsLeft=EH.cards_left(card1)-1
        nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
        player1,player2,nxtTurn=royal_mode(cardsLeft,nxtTurn,card2,storage,player1,player2)
        cardsLeft,storage = reset_variables()
        b = input('click space to continue')
        continue_game(b)
        nxtTurn,card2=turn(nxtTurn)
        card1=card2
    else:
        card1=card2

if len(player1)>0:
    print("player 1 won the game!")
else:
    print("player2 won the game!")
