# Alishya Xavier, Skill pracatice password validator



while True:
    password = input('Type in your password: ')
    if len(password) >= 8:
        print('Your password has passed the length check')
    else:
        print('Your password is not at least 8 characters')
        continue
    if '@' in password or '#' in password or '$' in password or '&' in password or '*' in password:
        print('Your password passed the special character')  
    else:
        print('Your password doesn\'t have at least one special character.')
        continue
    if '1' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password:
        print('Your password passed the at least one number check')
    else:
        print('Your password didn\'t pass the at least one number check.')
        continue
    if len(password) >= 8 and '@' in password or '#' in password or '$' in password or '&' in password or '*' in password and '1' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password:
        True
        print('Your password is strong enough!')
        break
    else:
        continue