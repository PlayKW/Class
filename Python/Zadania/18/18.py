# Import
from operator import contains

# Preparation
letterSet = list("abcdefghijklmnopqrstuvwxyz")
setLen = len(letterSet)
result = ""

# Initial input
inp = input("Type the message: ")
key = int(input("Give the key: "))

### Logic
# Word letter loop
for c in inp:

    isCap = c.isupper()
    # Is any translation?
    c = c.lower()
    if contains(letterSet,c):
        # Translate - new letter
        for i in range(0, setLen):
            if letterSet[i] == c:
                index = (i + key) % setLen
                if isCap:
                    result += letterSet[index].capitalize()
                else:
                    result += letterSet[index]
    # Is no translation?
    else:
        if isCap:
            result += c.capitalize()
        else:
            result += c

# End output
print("====================================")
print("* Message:\n")
print(result)