#Alishya Xavier, ProficiencyTest: Simple Quiz Game
score = 0
question1 = input('What is the most popular food in the United states? \n A. Grilled Cheese\n B. French Fries\n C. Steak \n D. Hamburgers\n')

if question1 == 'D':
    print('That is correct')
    score +=1
    question2 = input('What is the most popular soda in the United States? \n A. Coke\n B. Pepsi\n C. Sprite\n D. Dr. Pepper\n ')
    if question2 == 'A':
        print('That is correct!')
        score +=1
        question4 = input('What is the most popular chips in the United States? \n A. Fritos\n B. Takis\n C. Lay\'s \n D. Doritos\n ')
        if question4 == 'C':
            print('That is correct.')
            score+=1
            question5 = input('What is the most popular meat in the United States? \n A. Beef\n B. Chicken\n C. Pork\nD. Buffalo\n ')
            if question5 == 'B':
                print('That is correct!')
                score +=1
                question6 = input('What is the most popular appetizer in the United States? \n A. Wings\n B. Salad\n C. Cheese and Crackers\n D. Macaroni and Cheese\n ')
                if question6 == 'A':
                    print('That is correct!')
                    score+=1
            else:
                print('That is not correct.')

        else:
            print('That is not correct')
    else:
        print('That is incorrect.')
else:
    print('That is not correct')
    question3 = input('What is the most popular candy in the United States? \n A. Snickers\n B. Reese\'s Peanut Butter Cups \n C. Twix\n D. Nerds \n')
    if question3 == 'B':
        print('You got that correct!')
        score +=1
    else:
        print('That is incorrect.')

print('Your final score is', score,' out of 5.')
