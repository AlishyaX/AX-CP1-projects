#Alishya Xavier, Profiecency test Authorized

admin = ['Adelle', 'Sasha', 'Lila', 'Alishya', 'Maya', 'Jalaja', 'Ajash', 'Andrew']
not_authorized = ['Shan', 'Lisa']

user = input('What is your name?')

if user in admin:
    print('You are an admin.')
elif user in not_authorized:
    print('You are not authorized to log in.')
else:
    print('You are an user.')