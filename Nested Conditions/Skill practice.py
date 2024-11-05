#Alishya Xavier, Skill practice error handeling calculator

num1 = input('Type your first number: ')
num2 = input('Type your second number: ')
operation = input('Type in the operation you want to use: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    if operation == '+':
        print(int(num1) + int(num2))
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('This doesn\'t have an exact number answer.')
        else:
            print(num1 / num2)
    
except:
    print('Your input is not an integer.')