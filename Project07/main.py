import random

wordList = ['palavra']
lives = 6
randomWord = random.choice(wordList)

print('_'*len(randomWord))
display = ['_'] * len(randomWord)

while lives > 0 :
    guess = str(input('Type a letter: '))
    if guess in randomWord:    
        for index in range(len(randomWord)):
            if randomWord[index] == guess:
                display[index] = guess
        print(display)
        print(f'vidas: {lives}')
    else:
        lives-=1
        print(display)
        print(f'vidas: {lives}')
    if '_' not in display:
        print('Win!')
        print(f'vidas: {lives}')
        break
    if lives == 0:
        print('Lose!')


print(display)
