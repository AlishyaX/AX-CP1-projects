#Alishya Xavier, Final project
global name

health = 25
days = 7



def intro():
    name = input('Welcome to this Fantasy/Adventure game!\n What is your name: ')
    print('')
    start_mission = input('Are you ready to start your mission: (y/n) ')
    if start_mission == 'y':
        choices()

def choices():
    print('Here are all of the options for the places you can go:')

def safe_place():
    days -= .5
    health +=6
    print('This is the place you can go to rest and reenergize\n')
    print('When you come here your health will go up 6 points but you will lose half a day.\n')
    print('You now have',health,'')
    

def haunted_barn():

def inventory_barn():

def villages():

def riddles_barn():

def arena_one():

def arena_two():

def arena_three():

def arena_four():
