#Alishya Xavier, Final project
import time
items = []
inventory = []

health = 25
days = 7
life = 4
medals = 0

#This function I run evertime to see if the main_char has won the game yet or lost the game yet
def conclude():
    if medals == 4 and life > 0 and days >=0 and health >=0:
        print('After you completed the last battle, you found this underground passage way \nand rescued everyone that was trapped down there by the mythical creatures.')
        print('You have completed the mission')
        time.sleep(4)
        print('Congradulations! Your name will be forever remembered in the legacy!')
    elif life == 0 and health == 0:
        print('You have failed the mission because you died.')
    elif days == 0:
        print('You failed the mission because you ran out of time and everyone went missing so you were the last one.')
        
    else:
        choices()

def safe_place():
    global days, health
    days -= .5
    health +=6
    print('This is the place you can go to rest and re energize\n')
    print('When you come here your health will go up 6 points and you will lose half a day.\n')
    print('You now have', health,'health points and', days,'days left.')
    conclude()

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
        print('You open the box and find a flashlight that had the words "It\'s a scary world out there')
        f = input('Do you want to put the flashlight in your backpack(y/n):  ')
        if f == 'y':
            items.append('flashlight')
            print('You then left the barn.')
            print('Here are all of the items you have in your backpack:')
            print(items)
            
        elif f == 'n':
            print('You leave the barn.')
            
        else:
            print('That is not one of the options.')
            haunted_barn()
        
    else:
        print('That is not one of the options.')
        haunted_barn()
    print('You now have',health,'health points and',days,'days left.')
    conclude()


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
    conclude()

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
    print('Before you left the old man gave you ')
    days-=.5
    print('You now have',health,'health points and',days,'days left.')
    conclude()

def riddles_barn():
    global days, health,i
    days -=.5
    print('You now have',health,'health points and',days,'days left.')
    print('You walked around and found another abandoned barn.')
    time.sleep(1)
    print('As you walked through the creaky door you see this one safe that has the year 1993 on the top.')
    time.sleep(3)
    print('As you go to open it you see on the small screen the riddle:\nI have no voice, but I can speak to you.\nI have no life, but I can teach you.\nI have no eyes, but I can show you the world.\n')
    time.sleep(5)
    print('If you figure out what it is then you will be able to open the safe.')
    for i in range(9):
        safe = input('If you want to leave the game type leave\nWhat is the answer: ').lower()
        if safe == 'book' or safe == 'a book':
            print('That is correct')
            print('When you opened the safe you found this purple potion with a note that says use wisely!')
            potion = input('Do you want to put this in your backpack(y/n): ')
            if potion == 'y':
                if len(items) == 5:
                    print('You don\'t have any space in your backpack.')
                    conclude()
                else:
                    items.append('potion')
                    print('You have put the potion in your backpack.')
                    print('Here is everything in your backpack:')
                    print(items)
                    conclude()
            else:
                print('You left the riddles barn')
                conclude()
        elif safe == 'leave':
            break
        else:
            print('That is incorrect')
            print('This is your ',i+1,' attempt and you only have 9 attempts before it completly locks you out')
            if i == 8:
                print('You ran out of times you could try.')
                conclude()
            else: 
                continue
        


def dragon_cave():
    global life, days, medals
    days -=1
    print('Here are all of the items you have in your backpack:')
    print(items)
    if 'bow and arrow' in items:
        print('You have the required item that can be used during battle.')
    else:
        print('You don\'t have the required item.' )
    dragon_battle = input('Do you want to start the battle(y/n):')
    if dragon_battle == 'y':
        print('You decided to take a look at the mud footprints that followed all the way into this huge dark cave.')
        time.sleep(5)
        print('You see this bright red light coming out from inside every few seconds. ')
        time.sleep(4)
        print('You have already figured out that it is a dragon.')
        time.sleep(5)
        print('You quietly start to enter the cave as the snoring you were once hearing stopped.')
        time.sleep(4)
        print('It is too late to turn back so you just creep in very quietly.')
        time.sleep(4)
        print('When you peep the corner you see that the dragon is sleeping right in front of this big metal cage.')
        time.sleep(5)
        print('You also see that there is a broken chain from the dragons ankle and the wall.')
        time.sleep(5)
        print('When you try to peep again suddenly the dragon is gone!')
        time.sleep(9)
        print('Suddenly you feel this hot breath coming right on top of you.')
        time.sleep(6)
        dragon_choice_1 = input('What do you do? \n1. run\n2.play dead\n3. scream to scare it off\n')
        if dragon_choice_1 == '1':
            print('You ran to the opposite side as the dragon bursts fire throughout the cave')
            time.sleep(7)
            print('You found this small hole in the cave wall hidden by the other side of the cave.')
        elif dragon_choice_1 == '2':
            print('The dragon already knew that you were alive and didn\'t let you leave.')
            life =-1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        elif dragon_choice_1 == '3':
            print('The dragon got intimidated and decided to breath fire to you!')
            life -= 1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        else:
            print('That is not one of the options.')
            dragon_cave()
        print('That dragon looked everywhere for you but couldn\'t find you so decided to go back to sleeping.')
        time.sleep(6)
        dragon_d = input('What do you want to do:\n1. Leave\n2. Try to sneak around the dragon to go look at the cage\n3. Get an item from your backpack')
        if dragon_d == '1':
            print('While you were trying to sneak out the dragon caught you and breathed out fire before you could escape.')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        elif dragon_d == '2':
            print('While you were sneaking around the dragon woke up and breathed fire onto you!')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        elif dragon_d == '3':
            print('Here are the items in your backpack',items)
            i_g = input('Which item do you wat to take out of your backpack: ')
            if i_g == 'bow and arrow':
                print('You took the bow and arrow and snuck back to the cave wall hidden from the dragon.')
            else:
                print('You tried to use the item but it didn\'t work on the dragon and it ended up breathing fire on you')
                time.sleep(6)
                life -=1
                print('You lost one of your lifes and have been respawned.')
                print('You now have',life,' lives left.')
                conclude()
            print('While the dragon was sleeping you shot an arrow right at his heart as it instantly dies.')
            time.sleep(6)
            medals +=1
            print('You have recieved a medal and you only need 4 to complete the mission.')
            print('When you opened the cage you saw this beautiful conch with a note that says \n"use this when you are reday Serene, I love you"')
            conch = input('Do you want to put the conch in your backpack(y/n): ')
            if conch == 'y':
                if len(items) == 5:
                    print('You don\'t have enough space in your backpack.')
                    conclude()
                else:
                    items.append('conch')
                    print('This is what is in your backpack:')
                    print(items)
            else:
                print('You left the cave')
                conclude()
            print('After you were done, you left the cave.')
            conclude()
    else:
        conclude()


def tarton_sea():
    global life, days, medals
    days -=1
    print('Here are all of the items you have in your backpack:')
    print(items)
    if 'conch' in items:
        print('You have the required item that can be used during battle.')
    else:
        print('You don\'t have the required item.' )
    m = input('Do you want to start the battle(y/n):')
    if m == 'y':
        print('As you were walking around you heard this beautiful sound coming from the tarton sea.')
        time.sleep(5)
        print('The sound almost felt like it was pulling you in as you started mindlessly walking towards the sound.')
        time.sleep(7)
        print('As you were about to walk onto the sand beach the sound stopped and you suddenly collapsed in front of a bush.')
        time.sleep(5)
    else:
        conclude()
    print('As you slowly gained conscious you peeped over the bush to see a group of boys mindlessly walking forward.')
    time.sleep(5)
    print('When you looked at what they were walking towards, you remembered learning about them?')
    time.sleep(4)
    print('It looked like a mermaid of some sort, Oh wait you remember it is a siren.')
    time.sleep(7)
    siren_d = input('We have to do something to save the boys!\nWhich one do you want to do:\n1. Get an item out of your backpack\n2. Quickly get up and run at the siren to scare it off\n3. Go call for help to see if someone can help ')
    if siren_d =='1':
        print('Here are the items in your backpack',items)
        s_d = input('Which item do you wat to take out of your backpack: ')
        if s_d == 'conch':
            print('You took the conch and remembering all of the information given to you while training started to blow on one side.')
        else:
            print('You tried to use that item but then got caught by the siren and the siren controlled your mind.')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        time.sleep(7)
        print('Suddenly the boys broke out of the spell and started to run away.')
        time.sleep(4)
        print('Then the siren started getting light headed a bit so you blew harder')
        time.sleep(6)
        print('The siren\'s mind was spinning in circles as it collapsed on the floor, becoming unconscious forever.')
        medals+=1
        print('You have recieved a medal and you only need 4 to complete the mission.')
        print('You now have',medals,'medals.')
        conclude()
    elif siren_d == '2':
        print('While you were charging at the siren it suddenly saw you and managed to control your mind.')
        time.sleep(5)
        print('The siren then took control of you.')
        time.sleep(6)
        life -=1
        print('You lost one of your lifes and have been respawned.')
        print('You now have',life,' lives left.')
        conclude()
    elif siren_d == '3':
        print('As you were getting up to run away, the siren spotted you and was able to control your mind.')
        time.sleep(5)
        print('The siren then took control of you.')
        time.sleep(6)
        life -=1
        print('You lost one of your lifes and have been respawned.')
        print('You now have',life,' lives left.')
        conclude()
    else:
        print('That is not one of the options.')
        tarton_sea()
    

def forest():
    global life, days, medals
    days -=1
    print('Here are all of the items you have in your backpack:')
    print(items)
    if 'flashlight' in items:
        print('You have the required item that can be used during battle.')
    else:
        print('You don\'t have the required item.' )
    v_b = input('Do you want to start the battle(y/n):')
    if v_b == 'y':
        print('You were walking behind the villages when you heard some wierd sounds coming from the forest.')
        time.sleep(6)
        print('And then suddenly you heart these screams also coming from there.')
        time.sleep(7)
        print('You decide to go try to help so you start to run through the forest towards where you heard the sound coming from.')
        time.sleep(5)
        print('You then stop right in front of a tree, and as you peeked to the other side you saw this VAMPIRES!')
        time.sleep(10)
        print('There were also a bunch of kids crying on the ground being surrounded by them.')
        v = input('What do you do:\n1. Run out into the group and scare them off\n2. Make a distraction by throwing some sticks to the opposite side\n3. Go get help\n 4.Get something out of your backpack')
        if v == '1':
            print('The vampires all charged at you and caught you.')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
        elif v == '2':
            print('The vampires could smell a human and after hearing the sound coming from there, they left the kids tied and ran over there.')
            time.sleep(7)
            print('You then wernt and untied the children, letting them go back home quickly.')
            time.sleep(6)
            print('Right after the children left you heard the vampires coming back!')
            d = input('What do you do:\n1. Run\n2. Get something out of your backpack\n3. Hide')
            if d == 2:
                print('Here are the items in your backpack',items)
                s_d = input('Which item do you want to take out of your backpack: ')
                if s_d == 'flashlight':
                    print('You took the flashlight and when they came to you, you put it on the highest brightness.')
                    time.sleep(5)
                    print('They started getting frightened as you then chased them around.')
                    time.sleep(7)
                    print('Suddenly the vampires got stuck in some quick sand and were never saw again.')
                    medals+=1
                    print('You have recieved a medal and you only need 4 to complete the mission.')
                    print('You now have',medals,'medals.')
                    conclude()
                else:
                    print('You tried to use that item but then got caught by the vampires, leaving them a feast.')
                    time.sleep(6)
                    life -=1
                    print('You lost one of your lifes and have been respawned.')
                    print('You now have',life,' lives left.')
                    conclude()

            else:
                print('While you were doing that, the vampires found you and had a feast.')
                time.sleep(6)
                life -=1
                print('You lost one of your lifes and have been respawned.')
                print('You now have',life,' lives left.')
                conclude()
        else:
            print('As you were about to do that, the vampires saw you and charged at you, ending up catching you.')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()
    else:
        conclude()


def witches_castle():
    global life, days, medals
    days -=1
    print('Here are all of the items you have in your backpack:')
    print(items)
    if 'potion' in items:
        print('You have the required item that can be used during battle.')
    else:
        print('You don\'t have the required item.' )
    w_b = input('Do you want to start the battle(y/n):')
    if w_b == 'y':
        print('As you were walking around past the villages you saw this huge castle out completly in the middle of nowhere.')
    else:
        conclude()
    time.sleep(5)
    print('You decided to walk through the forest at night since you can\'t waste too much time.')
    time.sleep(5)
    print('As you were walking you heard a lot of wherewolves howling at the full moon.')
    time.sleep(4)
    print('When you finally got out of the trees, the huge dark castle was waiting ahead. ')
    time.sleep(7)
    print('You then decided to sneak up to the castle and go through the back door.')
    time.sleep(6)
    print('As you were walking up the stairs you heard cackling coming from the kitchen area.')
    time.sleep(7)
    print('You then ended up peeping the corner to see children trapped in a container ready to be put into a bubbling couldren with green liquid slipping out of it.')
    time.sleep(8)
    c = input('We have to do something before it is too late!\n What should we do:\n1. Get something out of your backpack\n2. quickly run in and grab the children\n3. Go attack the witch')
    if c == '1':
        print('Here are the items in your backpack',items)
        s_d = input('Which item do you want to take out of your backpack: ')
        if s_d == 'potion':
            print('You took the potion and when the witch left the room for a minute you put the potion in the stew.')
            time.sleep(5)
            print('Then when the witch came back and took a sip of her stew, she suddenly went unconscious and never woke up.')
            time.sleep(6)
            print('You then took the children and went back to the village and found their parents.')
            medals+=1
            print('You have recieved a medal and you only need 4 to complete the mission.')
            print('You now have',medals,'medals.')           
            conclude()
        else:
            print('You tried to use that item but then the witch caught you and got you ready for the stew.')
            time.sleep(6)
            life -=1
            print('You lost one of your lifes and have been respawned.')
            print('You now have',life,' lives left.')
            conclude()            

    elif c == '2':
        print('As you were running through the kitchen, the witch caught you and got you also ready for the stew.')
        time.sleep(6)
        life -=1
        print('You lost one of your lifes and have been respawned.')
        print('You now have',life,' lives left.')
        conclude()
    elif c == '3':
        print('You tried to attack the witch but the witch was all ready for you and put a spell on you.\nThen she got you alsp ready for the stew.')
        time.sleep(6)
        life -=1
        print('You lost one of your lifes and have been respawned.')
        print('You now have',life,' lives left.')
        conclude()


#This is the function that I keep running for the main_char to pick which place they want to go to 
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

# This is the introduction function that calls other functions that call others.    
def intro():
    global main_char
    main_char = input('Welcome to this Fantasy/Adventure game!\nWhat is your name:\n')
    print('So far', main_char,'has been training ever since he/she was a kid to be able to complete the hardest challenge of their lifetime. ')
    time.sleep(7)
    print('If you do complete the mission then you will be praised and have the honor of being an official armender.')
    start_mission = input('Are you ready to start your mission: (y/n) ')
    if start_mission == 'y':
        print('For your mission you will be sent to Aruna islands in a private jet.')
        time.sleep(6)
        print('It seems that people have been going missing and at this rate everyone on that island will be gone in 7 days. ')
        print('So in the end you will need to find the root cause of why people are going missing and fix it.')
        time.sleep(9)
        print('You have now reached The Aruna Islands!')
        conclude()
    else:
        breakpoint
intro()








 

