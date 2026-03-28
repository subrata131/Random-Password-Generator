import random
import string
symbol_are="!@#$%&*"
def get_password(length,digit,symbol):
    password=[]
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    
    character=string.ascii_letters
    if digit:
        password.append(random.choice(string.digits))
    
    
    if symbol:
        password.append(random.choice(symbol_are))

    character=string.ascii_letters
    if digit:
        character+=string.digits
    if symbol:
        character+=symbol_are

    for _ in range (length - len(password)):
        password.append(random.choice(character))
        random.shuffle(password)

    return "".join (password)

length=int(input("Enter Password Length:"))
digit=input("Include Digits? (Y/N):").lower()== "y"
symbol=input("Include symbols? (Y/N):").lower()== "y"
password=get_password(length,digit,symbol)
print("\n Password is =",password)


   
    
