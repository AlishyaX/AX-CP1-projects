#Alishya Xavier, Final project
global health, days
items = []
invetory = []

health = 25
days = 7

def safe_place():
    days -= .5
    health +=6
    print('This is the place you can go to rest and reenergize\n')
    print('When you come here your health will go up 6 points and you will lose half a day.\n')
    print('You now have', health,'health points and', days,'days left.')
    choices()

def haunted_barn():
    days -=.5
    print('You found a haunted barn when you were walking around\nand decided to walk in. You start invetigating the barn as you see\ndust everwhere. Suddenly you saw this light colored smoke enter the barn.\n  ')
    print('From all of your training you already knew that it was called an ectoplasm.\n')
    ectoplasm = input('You have two options:\n 1. Attack\n 2. Hide').lower()
    if ectoplasm == 'attack':
        print(' Since you couldn\'t see the ectoplasm it threw you all the way cross the barn\nand kicked you out of the barn, luckily sparing your life. ')
        health -=5
        print('Even though the ectoplasm spared your life, you still lost 5 health')

    elif ectoplasm == 'hide':
        print('The ectoplasm couldn\'t find you and decided to leave')
        print('As you were leaving, you found a dusty old box.')
        print('You open the box and find a key that had the letters written d r a g o n carved into it. ')
        key = input('Do you want to put the key in your backpack(y/n):  ')
        if key == 'y':
            items.append('key')
            print('You then left the barn.')
            print('Here are all of the items you have in your backpack:')
            print(items)
            
        elif key == 'n':
            print('You leave the barn.')
            
        else:
            print('That is not one of the options.')
            haunted_barn()
        
    else:
        print('That is not one of the options.')
        haunted_barn()
    print('You now have',health,'health points and',days,'days left.')
    choices()

def inventory_barn():
    

def villages():

def riddles_barn():

def arena_one():

def arena_two():

def arena_three():

def arena_four():

def choices():
    print('Here are all of the options for the places you can go:\n 1. The safe place\n 2. The haunted barn\n 3. The inventory barn\n 4. The villages\n 5. The riddles barn\n 6. Arena one\n 7. Arena two\n 8. Arena three\n 9. Arena four')
    go = input('Where do you want to go: ').lower()
    if go == 'the safe place':
        safe_place()
    elif go == 'the haunted barn':
        haunted_barn()
    elif go == 'the inventory barn':
        inventory_barn()
    elif go == 'the villages':
        villages()
    elif go == 'the riddles barn':
        riddles_barn()
    elif go == 'arena one':
        arena_one()
    elif go == 'arena two':
        arena_two()
    elif go == 'arena three':
        arena_three()
    elif go == 'arena four':
        arena_four()
    else:
        print('That was not one of the options')
        choices()
    
def intro():
    main_char = input('Welcome to this Fantasy/Adventure game!\nWhat is your name:\n')
    
    start_mission = input('Are you ready to start your mission: (y/n) ')
    if start_mission == 'y':
        choices()
    else:
        breakpoint
intro()








 

