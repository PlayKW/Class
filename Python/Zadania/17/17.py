# Import
from ctypes.wintypes import CHAR
from operator import contains
import random

### Preparation
wrds = []
usedChars = []
for x in range(1,21):
    wrds.append(f"slowko{x}")

pattern = random.choice(wrds)
label = ""
tries = 0

for c in pattern:
    label += '-'

# Visual elements
ftr = "=-------------------------------=\n"


### Game logic
while label != pattern:

    # Tries iteration
    tries += 1

    # Display
    display = ""
    for c in label:
        display += c + ' '
    
    print(ftr)
    print(display)
    print("Used:",usedChars)

    # Input
    inp = input("Question: ")

    # Letter select
    if len(inp) == 1:
        # Is lettern in a pattern?
        if inp in pattern:
            
            # List insert
            usedChars.append(inp)

            # Replace loop
            for i in range(0,len(pattern)):
                if inp == pattern[i]:

                    # Label index replace
                    s = list(label)
                    s[i] = inp
                    label = "".join(s)
                
                    # Is last letter?
                    if '-' not in s:
                        break

        # Fail message
        else:
            print(f"No matches found for letter '{inp}'")
    
    # Word select
    else:
        if inp == pattern:
            break
        else:
            print(f"Word {inp} is incorrect! Try again.")


### End
print(ftr)
print("Congratulations!")
print(f"The chosen word was {pattern}.")
print(f"It took you {tries} tries to guess it!")
