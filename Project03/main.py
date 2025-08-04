print('Welcome to Treasure Island')
direction = str(input('Move for left ou right? '))
directionLower = direction.lower()
if directionLower == "right":
    print('You fall into a hole ')
elif directionLower == 'left':
    action1 = input('Do you swim or wait? ')
    if action1 == 'swim':
        print('Attacked by trout ')
    elif action1 == 'wait':
        action2 = input('Which door you choses? ')
        if action2 == 'Red':
            print('Burned by fire ')
        if action2 ==  'Yellow':
            print('You found the treasure! ')
        if action2 == 'Blue':
            print('Eaten by beasts! ')
        else: 
            print('Game over')
    else:
        print('Game over')