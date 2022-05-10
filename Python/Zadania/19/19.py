# Import
from operator import contains
import os
import string

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


def login(name:str,pin:str,accList:list):
    for acc in accList:
        if name == acc.name and pin == acc.pin:
            account = acc
            print(f"Logged as \"{name}\" ({acc.value})")
            return True
    
    print("Incorrect username or pin.")
    return False


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
running = True

while running:
    # Login
    while not logged:

        print("====- Login -====")
        username = input("Username: ")
        for acc in accs:
            if acc.name == username:
                pin = input("Pin: ")
                logged = login(username, pin, accs)
                break
        
        if not logged:
            print(f"User registered as \"{username}\" dosen't exist!")
            cmd = input(f"Do you want to register new account?[Y/n] ")
            cmd = cmd.lower()

            # Register
            if cmd == "y":
                while True:
                    print(f"Username: {username}")
                    pin = input("Pin: ")
                    nPin = input("Confirm pin: ")
                    if pin == nPin:
                        accs.append(Account(username, pin, 0))
                        print(f"New account \"{username}\" created!")
                        logged = login(username, pin, accs)
                        break
                    else:
                        print("Failed to create an account!")
                        cmd = input("Try again?[ /n] ")
                        cmd = cmd.lower()
                        if cmd == "n":
                            cmd = ""
                            break

    # Command reading
    while logged:
        cmd = input("--> ")
        if cmd == "logout":
            logged = False
        elif cmd == "exit":
            running = False
            break
        elif cmd == "send":
            address = input(f"From {username} to ")
            value = float(input("[$]"))
            for a in accs:
                if a.name == address:
                    send(account, a, value)
                    break
        else:
            print(f"Command \'{cmd}\' does not exist!")


# Final save
lines = []
linesAppended = 0
for acc in accs:
    if linesAppended == 0:
        lines.append(acc.name)
    else:
        lines.append("\n" + acc.name)
    lines.append("\n" + acc.pin)
    lines.append("\n" + str(acc.value))
    linesAppended += 1

file = open(loc,'w')
file.writelines(lines)
file.close()