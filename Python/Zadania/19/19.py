# Import
from operator import contains
import os
import string

# Def
class Account:
    def __init__(self, name:string, pin:string, value:float):
        self.name = name
        self.pin = pin
        self.value = value

def send(src:Account, dest:Account, value:int):
    if value > 0:
        src.value -= value
        dest.value += value


### Preparation
# File read
loc = os.getcwd() + "/Class/Python/Zadania/19/acc.txt"
file = open(loc)

#L ines detach 
contents = file.readlines()
file.close()
accs = []
i = 0

# Data read
while i < len(contents):
    acc = Account(contents[i],contents[i+1],(float)(contents[i+2]))
    accs.append(acc)
    i += 3

### Logic
# Access
username = pin = ""
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
            print(f"Username: {username}")
            pin = input("Pin: ")
            nPin = input("Confirm pin: ")
            if pin == nPin:
                


