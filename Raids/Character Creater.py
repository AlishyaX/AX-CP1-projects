#Alishya Xavier, Raid: Charcter Creater
h = 0
s = 0
d = 0
i = 0
class_choice = input('Choose one of these classes(Warrior,Wizard, Paleden, Ranger, or Rouge): ')
if class_choice == 'Warrior':
    h+=10
    s+=5
    d+=4
    i+=15
    print(' Health: 10\n Strength: 5\n Dexterity: 4\n Intelligence: 15')
elif class_choice == 'Wizard':
    h+=25
    s+=1
    d+=6
    i+=30
    print(' Health: 25\n Strength: 1\n Dexterity: 6\n Intelligence: 30')
elif class_choice == 'Paleden':
    h+=8
    s+=10
    d+=4
    i+=10
    print(' Health: 8\n Strength: 10\n Dexterity: 4\n Intelligence: 10')
elif class_choice == 'Ranger':
    h+=10
    s+=8
    d+=2
    i+=5
    print(' Health: 10\n Strength: 8\n Dexterity: 2\n Intelligence: 5')
elif class_choice == 'Rouge':
    h+=20
    s+=7
    d+=10
    i+=15
    print(' Health: 20\n Strength: 7\n Dexterity: 10\n Intelligence: 15')
else:
    print('That is not an option.')
race_choice = input('Choose one of these race\'s(Humans, Elves, Dwarves, Halfling): ')
if race_choice == 'Humans':
    h+=10
    s+=5
    d+=1
    i+=10
    print(' Health: 10\n Strength: 5\n Dexterity: 1\n Intelligence: 10')
elif race_choice == 'Elves':
    h+=25
    s+=2
    d+=8
    i+=25
    print(' Health: 25\n Strength: 2\n Dexterity: 8\n Intelligence: 25')
elif race_choice == 'Dwarves':
    h+=20
    s+=4
    d+=5
    i+=20
    print(' Health: 20\n Strength: 4\n Dexterity: 5\n Intelligence: 20')
elif race_choice == 'Halfling':
    h+=10
    s+=10
    d+=9
    i+=13
    print(' Health: 10\n Strength: 10\n Dexterity: 9\n Intelligence: 13')
else:
    print('That is not an option.')
name = input('What is your characters name? ')
print('Your character name is',name,'who is a',class_choice, race_choice)
print(' your final health is :',h,'\n your final strength is:',s,'\n your final dexterity is:',d,'\n your final intelligence is:',i,'')
