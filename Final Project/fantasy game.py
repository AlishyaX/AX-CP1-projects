#Alishya Xavier, Final project
import time
items = []
inventory = []

health = 25
days = 7



def safe_place():
    global days, health
    days -= .5
    health +=6
    print('This is the place you can go to rest and re energize\n')
    print('When you come here your health will go up 6 points and you will lose half a day.\n')
    print('You now have', health,'health points and', days,'days left.')
    choices()

def haunted_barn():
    global days, health
    days -=.5
    print('You found a haunted barn when you were walking around\nand decided to walk in. You start invetigating the barn as you see\ndust everwhere. Suddenly you saw this light colored smoke enter the barn.\n  ')
    print('From all of your training you already knew that it was called an ectoplasm.\n')
    ectoplasm = input('You have two options:\n 1. Attack\n 2. Hide\n')
    if ectoplasm == '1':
        print('3Since you couldn\'t see the ectoplasm it threw you all the way cross the barn\nand kicked you out of the barn, luckily sparing your life. ')
        health -=5
        print('Even though the ectoplasm spared your life, you still lost 5 health')

    elif ectoplasm == '2':
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
    global days, health
    print('As you walk into the barn there are dusty shelves all around and it seems that it used to \n belong to someone as you find an item on the shelf. You walk over to it. ')
    print('The item is a bow and arrow.')
    bow_and_arrow = input('Do you want to put the bow and arrow in your backpack(y/n): ')
    if bow_and_arrow == 'y':
        if len(items) == 5:
            print('Your backpack is full')
        else:
            items.append('bow and arrow')
            print('Here are all of the items you have in your backpack:')
            print(items)
    else:
        print('You left the bow and arrow there.')
    inventory_switch = input('Do you want to put any items in your backpack in your inventory(y/n):')
    if inventory_switch == 'y':
        print('These are all of the items you have in your backpack')
        print(items)
        switch = input('Which item would you like to put in your inventory:')
        if switch in items:
            print('This item is now in your inventory')
            inventory.append(switch)
        else:
            print('You don\'t have that item in your backpack')
    else:
        print('These are the things in your backpack:')
        print(items)
    inventory_place = input('Do you want to place anything in your backpack form your inventory(y/n): ')
    if inventory_place == 'y':
        print('These are all of the items in your inventory: ')
        print(inventory)
        place = input('Which item in your inventory would you like to put in your backpack? ')
        if len(items) == 5:
            print('You don\'t have nay space to put it in your backpack')
        else:
            if place in inventory:
                print('This item is now in your backpack')
                items.append(place)
            else:
                print('That item is not in your inventory.')
    else:
        print('These are all of the things in your inventory: ')
        print(inventory)
    days -=.5
    print('You now have',health,'health points and',days,'days left.')
    choices()


def villages():
    global main_char, health, days
    print('As you were walking around you decided to go towards the villages.\n There was a huge group of villagers surrounding eachother as they were all discussing\nsomething. You decided to go up to them and talk to them about it.')
    print('You asked on one of the old men about what they were talking about.')
    time.sleep(2)
    print('Old man: Do you know about what has been happening lately?')
    time.sleep(2)
    print(main_char,': Yes I have heard how people are going missing. Have you found out any other information?')
    time.sleep(2)
    print('Old man: Yesterday night we heard horrible noises and today when we all came out we saw these huge footprints \nof mud and it follows all the way to this dark cave that none have us have dared to go through.')
    time.sleep(2)
    print(main_char,': I can\'t believe all of that happened but don\'t worry I will figure out how to fix it')
    time.sleep(2)
    days-=.5
    print('You now have',health,'health points and',days,'days left.')
    choices()


def riddles_barn():
    global days, health
    days -=.5
    print('You now have',health,'health points and',days,'days left.')
    print('You walked around and found another abandoned barn.')
    time.sleep(1)
    print('As you walked through the creaky door you see this one safe that has the year 1993 on the top.')
    time.sleep(3)
    print('As you go to open it you see on the small screen the riddle:\nI have no voice, but I can speak to you.\nI have no life, but I can teach you.\nI have no eyes, but I can show you the world.\n')
    time.sleep(5)
    print('If you figure out what it is then you will be able to open the safe.')
    for i in range(10):
        safe = input('What is the answer: ').lower()
        if safe == 'book' or safe == 'a book':
            print('That is correct')
            print('When you opened the safe you found this purple potion with a note that says use wisely!')
            potion = input('Do you want to put this in your backpack(y/n): ')
            if potion == 'y':
                if len(items) == 5:
                    print('You don\'t have any space in your backpack.')
                    choices()
                else:
                    items.append('potion')
                    print('You have put the potion in your backpack.')
                    print('Here is everything in your backpack:')
                    print(items)
                    choices()
            else:
                print('You left the riddles barn')
                choices()
        else:
            print('That is incorrect')
            print('This is your ',i+1,' attempt and you only have 9 attempts before it completly locks you out')
            continue
        if i =='9':
            print('You ran out of times you could try.')
            choices()
        else: 
            continue

'''
def dragon_cave():

def witches_castle():

def forest():

def tarton_sea():
'''

def choices():
    print('Here are all of the options for the places you can go:\n 1. The safe place\n 2. The haunted barn\n 3. The inventory barn\n 4. The villages\n 5. The riddles barn\n 6. The dragon cave\n 7. The witches castle\n 8. The forest\n 9. The Tarton Sea')
    go = input('Where do you want to go: ')
    if go == '1':
        safe_place()
    elif go == '2':
        haunted_barn()
    elif go == '3':
        inventory_barn()
    elif go == '4':
        villages()
    elif go == '5':
        riddles_barn()
    elif go == '6':
        dragon_cave()
    elif go == '7':
        witches_castle()
    elif go == '8':
        forest()
    elif go == '9':
        tarton_sea()
    else:
        print('That was not one of the options')
        choices()
    
def intro():
    global main_char
    main_char = input('Welcome to this Fantasy/Adventure game!\nWhat is your name:\n')

    start_mission = input('Are you ready to start your mission: (y/n) ')
    if start_mission == 'y':
        choices()
    else:
        breakpoint









 

