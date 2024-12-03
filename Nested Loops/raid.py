# alishya xavier, Raid Multiplication table
for row in range(0, 13):
    for col in range(0, 13):
        num = row * col
        if num < 13:
            empty = "  "
        else:
            if num < 100: 
                empty  = " " 
        if col == 0:
            if row == 0:
                print("    ", end = '')
            else:
                print("  ", row, end='')
        elif row == 0:
            print("  ", col, end='')
        else:
            print(empty, num, end = '')
    print()

#I know we have to use the format option but I wasn't able to understand how to exactly put it in the code.
#{x:0=3d}