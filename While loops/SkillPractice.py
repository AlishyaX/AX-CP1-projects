#Alishya Xavier, Password Validator

i = 0
while i < 1:
    password = input('Type in your new password: ')
    if len(password) >= 8:
        print('Your password has passed the length check.')
        for i in password:
            if i == '@' or i == '#' or i == '$' or i == '%' or i == '*' or i == '&':
                print('Your password passed the special character check.')
            else:
                print('Your password doesn\'t have at least one special character.')
    else:
        print('Your password doesn\'t at least have 8 charcters.')
    if password == 