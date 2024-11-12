#Alishya Xavier, ProfieciencyTest: Shopping list manager

shopping_list = []

while True:
    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":
        add = input('What would you like to add? ')
        shopping_list.append(add)
        print(shopping_list)
    elif action =="2":
        rem = input('What would you like to remove? ')
        shopping_list.remove(rem)
        print(shopping_list)
    else:
        print("Have a nice day!")
        break