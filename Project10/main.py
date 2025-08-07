def sum(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2 == 0:
        return 'Invalid denominator'
    else:
        return num1/num2
    
running = True

operationDictionary = {
    '+': sum,
    '-': subtraction,
    '*': multiply,
    '/': divide
}
num1 = float(input('Please input the first number: '))

while running:
    num2 = float(input('Please input the second number: '))
    operator = str(input('Which operation do you want realize? "+" "-" "*" "/" \n'))
    answer = operationDictionary[operator](num1,num2)
    print(f'{num1} {operator} {num2} = {answer}')
    run = str(input('If you want exit, please type: "exit"\nType "yes" to continue: \n'))
    if run == 'exit':
        running = False
    if run == 'yes':
        num1 = answer
    