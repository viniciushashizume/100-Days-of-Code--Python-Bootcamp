bill = float(input('What was the total bill? '))
tip = float(input('How much tip would you like to give? '))
billSplit = float(input('How many people to split the bill? '))
eachPayment = (bill+tip) / billSplit
print(f'Each person should pay: {eachPayment}')