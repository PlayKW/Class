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
    newC = c.lower()
    # Is any translation?
    if contains(letterSet,c):
        # Translate - new letter
        for i in range(0, setLen):
            if letterSet[i] == c:
                index = (i + key) % setLen
                result += letterSet[index]
    # Is no translation?
    else:
        result += c

# End output
print("====================================")
print("* Message:\n")
print(result)