import EgyptionWarHelper

def continue_game(input):
    while input != ' ':
        input = input('click space to continue')


def royal_mode(cardsLeft,nxtTurn,card,storage,deck1,deck2):
    player1,player2=deck1,deck2
    card1 = card
    card2 = ''
    if len(deck1)<cardsLeft:
        cardsLeft=len(deck1)

    if EgyptionWarHelper.check_slaps(storage):  # Slaps
        EgyptionWarHelper.print_winner(nxtTurn, storage)
        if nxtTurn == 'player1':
            player1 = storage + deck1
        else:
            player2 = storage + deck2
        cardsLeft, storage = reset_variables()
    elif EgyptionWarHelper.is_royal(card1):
        nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
        cardsLeft = EgyptionWarHelper.cards_left(card1)

    while cardsLeft > 0:
        b = input('click space to continue')
        continue_game(b)
        if nxtTurn == 'player1':  # Who needs to pull out the cards
            card2,deck1 = EgyptionWarHelper.pull_out_card(deck1, nxtTurn)
        else:
            card2,deck2 = EgyptionWarHelper.pull_out_card(deck2, nxtTurn)
        storage.append(card2)
        cardsLeft = cardsLeft - 1
        card1 = card2

        if EgyptionWarHelper.check_slaps(storage):
            nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'# Slaps
            EgyptionWarHelper.print_winner(nxtTurn, storage)
            if nxtTurn == 'player1':
                player1 = storage + deck1
            else:
                player2 = storage + deck2
            cardsLeft,storage = reset_variables()
            break
        elif EgyptionWarHelper.is_royal(card1):
            nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
            cardsLeft = EgyptionWarHelper.cards_left(card1)


    if len(storage)!=0:#If the loop was stopped because cardsLeft>0 and not break
        nxtTurn = 'player2' if nxtTurn == 'player1' else 'player1'
        EgyptionWarHelper.print_winner(nxtTurn, storage)
        if nxtTurn == 'player1':
            player1 = storage + deck1
        else:
            player2 = storage + deck2

    return player1,player2



def reset_variables():
    cardsLeft = 0
    storage = []
    return cardsLeft,storage


def main():
    #Decks
    while True:
        try:
            print('Click space to play a normal game')
            print('Enter the amount(1-25) of cards you want for each player.')
            N = input()
            if N == ' ':
                N = 26
                print(N)
                break
            else:
                N = int(N)
                if N <= 26 and N > 0:
                    break
        except ValueError:
            print('Please enter a number ')
        else:
            print('Please enter a number between 1 and 25 or click space')
    player1 = []#player1's deck
    player2 = []#player2's deck
    player1, player2 = EgyptionWarHelper.create_decks(player1, player2, N)


    cardsLeft = 0#How many cards does the current player have left to draw out while the other one has drew a royal.
    storage = []#Stores the current cards that the winner will get.

    #The first card
    nxtTurn = 'player1'#Stores the name of the player that should draw a card next.
    card1 ,player1= EgyptionWarHelper.pull_out_card(player1,nxtTurn)#Stores the card that is checked at the current turn
    card2=''#stores the card that has been drew now.
    nxtTurn = 'player2'
    storage.append(card1)

    #The game
    while len(player1)>0 and len(player2)>0:
        b = input('click space to continue')
        continue_game(b)

        if nxtTurn == 'player1':
            card2, player1 = EgyptionWarHelper.pull_out_card(player1,nxtTurn)
            nxtTurn = 'player2'
        else:
            card2, player2 = EgyptionWarHelper.pull_out_card(player2,nxtTurn)
            nxtTurn = 'player1'
        storage.append(card2)

        #Normal slaps
        if EgyptionWarHelper.check_slaps(storage):
            EgyptionWarHelper.print_winner(nxtTurn,storage)
            if nxtTurn == 'player1':
                player1 = storage + player1
            else:
                player2 = storage + player2
            cardsLeft,storage = reset_variables()
            if nxtTurn == 'player1':
                card2, player1 = EgyptionWarHelper.pull_out_card(player1, nxtTurn)
                storage.append(card2)
                nxtTurn = 'player2'
            else:
                card2, player2 = EgyptionWarHelper.pull_out_card(player2, nxtTurn)
                storage.append(card2)
                nxtTurn = 'player1'
            card1 = card2
            continue
        #Royals
        if EgyptionWarHelper.is_royal(card1):
            cardsLeft=EgyptionWarHelper.cards_left(card1)-1
            nxtTurn = 'player1' if nxtTurn == 'player2' else 'player2'
            player1,player2 = royal_mode(cardsLeft,nxtTurn,card2,storage,player1,player2)
            cardsLeft,storage = reset_variables()
            b = input('click space to continue')
            continue_game(b)
            if nxtTurn == 'player1':
                card2, player1 = EgyptionWarHelper.pull_out_card(player1, nxtTurn)
                storage.append(card2)
                nxtTurn = 'player2'
            else:
                card2, player2 = EgyptionWarHelper.pull_out_card(player2, nxtTurn)
                storage.append(card2)
                nxtTurn = 'player1'
            card1 = card2
        else:
            card1=card2

    if len(player1)>0:
        print("player 1 won the game!")
    else:
        print("player2 won the game!")
if __name__ == '__main__':
        main()