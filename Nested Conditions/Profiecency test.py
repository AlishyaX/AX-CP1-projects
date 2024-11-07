#Alishya Xavier, ProficiencyTest: Simple Quiz Game
score = 0
global question1, question2, question3, question4, question5, question6
question1 = input('What is the most popular food in the United states? \n A. Grilled Cheese\n B. French Fries\n C. Steak \n D. Hamburgers\n')

if question1 == 'D':
    print('That is correct')
    score +=1
    
else:
    print('That is not correct')
    question2 = input('What is the most popular soda in the United States? \n A. Coke\n B. Pepsi\n C. Sprite\n D. Dr. Pepper\n ')
    if question2 == 'A':
        print('That is correct!')
        score +=1
    else:
        print('That is incorrect.')
question4 = input('What is the most popular chips in the United States? \n A. Fritos\n B. Takis\n C. Lay\'s \n D. Doritos\n ')
if question4 == 'C':
    print('That is correct.')
    score+=1
else:
    print('That is incorrect.')
    question5 = input('What is the most popular meat in the United States? \n A. Beef\n B. Chicken\n C. Pork\n D. Buffalo\n ')
    if question5 == 'B':
        print('That is correct!')
        score +=1
    else:
        print('That is incorrect.')
question6 = input('What is the most popular appetizer in the United States? \n A. Wings\n B. Salad\n C. Cheese and Crackers\n D. Macaroni and Cheese\n ')
if question6 == 'A':
    print('That is correct!')
    score+=1
else:
    print('That is not correct.')
    question7 = input('What is the most popular ice cream flavor in the United States?\n A. Vanilla\n B. Strawberry\n C. Chocolate\n D. Cake batter\N')
    if question7 == 'A':
        print('That is correct.')
        score+=1
    else:
        print('That is not correct.')
question8 = input('What is the most popular dessert in the United States?\n A. Cake\n B. Ice Cream\n C. Cookies\n D. Cupcakes\n ')
if question8 == 'B':
    print('That is correct!')
    score+=1
else:
    print('That is incorrect.')
    question9 = input('What is the most popular type of pie in the United States? \n A. Coconut Cream\n B. Cherry\n C. Apple\n D. Pumpkin\n ')
    if question9 == 'C':
        print('That is correct!')
        score+=1
    else:
        print('That is not correct.')
question3 = input('What is the most popular candy in the United States? \n A. Snickers\n B. Reese\'s Peanut Butter Cups \n C. Twix\n D. Nerds \n')
if question3 == 'B':
    print('You got that correct!')
    score +=1
else:
    print('That is incorrect.')

print('Your final score is', score,'out of 5.')
