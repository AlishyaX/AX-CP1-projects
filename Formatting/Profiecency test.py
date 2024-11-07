#Alishya Xavier, Profiecency test what are these numbers

num = float(input('Type in a number:'))

txt1 = "This is it as an integer: {:,}"
print(txt1.format(num))

txt2 = "This is it as a percentage: {:.0%}"
print(txt2.format(num))

txt3 = "This is it as a dollar amount: {:,.2f}"
print(txt3.format(num))

txt4 = "This is it as a float with 4 decimal places: {:.4f}"
print(txt4.format(num))