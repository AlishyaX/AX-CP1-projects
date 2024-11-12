#Alishya Xavier, ProficiencyTest: Secret Cypher

def cypher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = ""
    code = str(input("Type in the code that you want translated: "))
    for char in code:
        char = ord(char)+7
        new_alphabet = new_alphabet+(chr(char))
    print("original code:",code)
    print("cyphered code:", new_alphabet)
cypher()







