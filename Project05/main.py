import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z']
numbers =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols =  ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')']

letterSize = int(input('lettersize: '))
numberSize = int(input('numbersize: '))
symbolsSize = int(input('symbolssize: '))

password = []

for letter in range(0, letterSize):
    password.append(random.choice(letters))

for number in range(0, numberSize):
    password.append(random.choice(numbers))

for letter in range(0, symbolsSize):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
password_print = ''
for char in password:
    password_print += char

print(password_print)
