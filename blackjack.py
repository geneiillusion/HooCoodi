#testailuja

import random
from tracemalloc import start

money = int(250)

numbers = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

shapes = ('Spades', 'Clubs', 'Hearts', 'Diamonds')

def bet_function(bet):
    print('How much you want to bet?')
    bet_amount = input('Betting' + bet)
    int(money) - int(bet)

while True:
    card1=[]
    card2=[]
    card3=[]

    card1draw = random.choice(numbers), 'of', random.choice(shapes)
    card1.append(card1draw)

    card2draw = random.choice(numbers), 'of', random.choice(shapes)
    card2.append(card2draw)

    hand = card1, card2

    startgame = input('''Do you want to start a new game? (Y)es or (N)o:
> ''')

    if startgame == 'Y':
        print('Your hand is following:', hand)
        action = input('''(D)raw a card, (B)et, (F)old or (S)tay
> ''')
        while True:

            if action == 'D':
                print('You draw a card . . .')
                card3draw = random.choice(numbers), 'of', random.choice(shapes)
                card3.append(card3draw)
                print('your card is: ', card3)

            elif action == 'B':
                bet_given = input('Place your bet: ')
                bet_function(bet_given)
                print('Money left: ', money)
                continue

            elif action == 'F':
                print('You folded you cards: ', hand)
                break

            elif action == 'S':
                print('You stau with your cards: ', hand)

            else:
                print(action, ' is not valid option')

    elif startgame == 'N':
        print('Thank you for playing! Quiting the game . . .')
        break
    else:
        print(startgame, 'is not valid option')