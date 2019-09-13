import random
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9',
             '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4',
             '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SLAPS7 = ('43', '34')
ROYALS = ('J', 'Q', 'K', 'A')


def random_card():
    r = random.randint(0, len(CARDS) - 1)
    card = CARDS[r]
    del CARDS[r]
    return card


def create_decks(p1,p2,amountOfCards=26):
    for i in range(amountOfCards):
        p1.append(random_card())
        p2.append(random_card())
    return p1,p2


def check_slaps(storage):
    if len(storage)>=2:
        if str(storage[-1])+str(storage[-2]) == str(SLAPS7[0]) or (str(storage[-1]) + str(storage[-2]) == str(SLAPS7[1])):
            return True
        elif storage[-1] == storage[-2]:#Same cards
            return True
    if len(storage)>=3:
            if storage[-1] == storage[-3]:#Sandwich
                return True
    return False


def is_royal(card): #also how many cards are left to summon untill lose
    for royal in ROYALS:
        if card == royal:
            return True
    return False


def cards_left(card):
    if card == 'A':
        return 4
    elif card == 'K':
        return 3
    elif card == 'Q':
        return 2
    else:#'J'
        return 1

def get_storage(storage,cardsPlaced,player1,player2):
    if check_slaps(storage):
        if cardsPlaced % 2 == 0:
            print(f'player 1 won the storage:{storage}')
            player1 = player1 + list(storage)
        else:
            print(f'player 2 won the storage:{storage}')
            player2 = player2 + list(storage)


def pull_out_card(deck, name):
    card = deck[0]
    del deck[0]
    print(f'{name}:{card}')
    return card


def won_round(storage,deck):
    deck=deck+storage

def print_winner(name,storage):
    print(f'{name} won the storage:{storage}')

