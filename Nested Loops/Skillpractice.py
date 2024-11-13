#Alishya Xavier, SkillPractice: Counting characters
a = 0
b = 0
c = 0
d = 0
e = 0
grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]

for i in grid:
    for letter in i:
        if 'A' == letter:
            a+=1
        elif 'B' == letter:
            b+=1
        elif 'C' == letter:
            c+=1
        elif 'D' == letter:
            d+=1
        elif 'E' == letter:
            e+=1
        else:
            break
print('A:', a, 'B:', b,'C:', c, 'D:',d, 'E:', e)
