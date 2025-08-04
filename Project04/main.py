import random

choice = int(input('0- Rock \n1- Paper \n2 - Scissors? '))
randomChoice = random.randint(0,2)
print (f'Your choice: {choice}')

if choice == randomChoice:
    print(f'AI Choice: {randomChoice} ')
    print('Draw')
elif (choice == 0 and randomChoice == 2) or (choice == 1 and randomChoice == 0) or (choice == 2 and randomChoice == 1):
    print(f'AI Choice: {randomChoice} ')
    print('Win')
else: 
    print(f'AI Choice: {randomChoice} ')
    print('LOse')