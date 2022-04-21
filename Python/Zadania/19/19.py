# Import
from operator import contains
import os
import string
from telnetlib import DO

# Def
class Account:
    def __init__(self, name:str, pin:str, value:float):
        self.name = name
        self.pin = pin
        self.value = value

def send(src:Account, dest:Account, value:int):
    if value > 0:
        src.value -= value
        dest.value += value

def insert(dest:Account, value:int):
    if value > 0:
        dest.value += value

def spend(src:Account, value:int):
    if value > 0:
        src.value -= value


def login(name:str,pin:str):
    for acc in accs:
        if name == acc.name and pin == acc.pin:
            account = acc
            print(f"Logged as \"{name}\" ({acc.value})")
            return True
        else:
            print("Incorrect username or pin.")
            return False;


### Preparation

# Accounts
account = Account("","",0)
accs = []

# File read
loc = os.getcwd() + "/Class/Python/Zadania/19/acc.txt"
file = open(loc)
contents = file.readlines()
file.close()

# Data read
i = 0
lineCount = len(contents)
while i < lineCount:
    if lineCount >= 3 and lineCount % 3 == 0:
        acc = Account(contents[i],contents[i+1],(float)(contents[i+2]))
        accs.append(acc)
        i += 3
    else:
        break

### Logic
# Access
username = pin = ""
logged = False

while True:
    username = input("Username: ")
    if contains(contents, username):
        pin = input("Pin: ")
    else:
        print(f"User registered as \"{username}\" dosen't exist!")
        cmd = input(f"Do you want to register new account?[Y/n]: ")
        cmd = cmd.lower()

        # Register
        if cmd == "y":
            while not logged:
                print(f"Username: {username}")
                pin = input("Pin: ")
                nPin = input("Confirm pin: ")
                if pin == nPin:
                    accs.append(Account(username, pin, 0))
                    print(f"New account \"{username}\" created!")
                    logged = True
                else:
                    print("Failed to create an account, repeat: ")
    
    # Final login
    logged = login(username, pin)
    break

lines = []
for acc in accs:
    lines.append(acc.name + "\n")
    lines.append(acc.pin + "\n")
    lines.append(str(acc.value) + "\n")

file = open(loc,'a')
file.writelines(lines)
file.close()



            
                


