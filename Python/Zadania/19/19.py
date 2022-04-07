# Import
import os
import string

# Def
class Account:
    def __init__(self, name:string, pin:string, value:int):
        self.name = name
        self.pin = pin
        self.value = value

def send(src:Account, dest:Account, value:int):
    if value > 0:
        src.value -= value
        dest.value += value


### Preparation
# File read
mainLoc = os.path.abspath() + '/'
os.makedirs(mainLoc + "acc")
files = os.listdir(mainLoc + "acc")

accs = []
for file in files:
    obj = open(file)
    name = obj.read()
    pin = obj.read()
    value = obj.read()
    acc = Account(name, pin, value)

ans = ''

### Logic


