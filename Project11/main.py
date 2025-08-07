import random

cards = {
    'A' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, 
    '7' : 7, '8' : 8, '9' : 9, 'Q' : 10, 'J' : 10, 'K' : 10
}

def drawCard(deck):
    """Seleciona uma carta aleatória do baralho e retorna sua chave e valor."""
    cardKey, cardValue = random.choice(list(deck.items()))
    return cardKey, cardValue

def showHands(playerCards, playerTotal, computerCards, computerTotal):
    """Exibe as cartas e a pontuação total do jogador e do computador."""
    print(f'Player cards: {playerCards} | Total: {playerTotal}')
    print(f'Computer cards: {computerCards} | Total: {computerTotal}')
    print("-" * 30) 


playerCards = []
computerCards = []
totalPlayer = 0
totalComputer = 0
running = True

while running:
    cardKey, cardValue = drawCard(cards)
    playerCards.append(cardKey)
    totalPlayer += cardValue

    cardKey, cardValue = drawCard(cards)
    computerCards.append(cardKey)
    totalComputer += cardValue

    showHands(playerCards, totalPlayer, computerCards, totalComputer)
    if totalPlayer == 21 or totalComputer > 21:
        print('You win!')
        break
    if totalComputer == 21 or totalPlayer > 21:
        print('You lose!')
        break
    
    draw = str(input('Do you want to buy one more card? "y" or "n": '))
    if draw.lower() == 'n':
        running = False
    elif draw.lower() == 'y':
        continue
    else:
        print('Invalid input')
        draw = str(input('Do you want to buy one more card? "y" or "n": '))