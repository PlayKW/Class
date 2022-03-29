# Import
from ctypes.wintypes import CHAR
import random

# Preparation
wrds = []
usedChars = []
for x in range(1,21):
    wrds.append(f"slowko{x}")

pattern = random.choice(wrds)
label = ""

for c in pattern:
    label += '-'


# Game logic
while label != pattern:

    # Display
    display = ""
    for c in label:
        display += c + ' '
    
    print("=-------------------------------=\n")
    print(display)
    print("Used: ",)

    # Input
    char = input("Given letter: ")

    # Letter select
    selectedAny = False
    for i in range(0,len(pattern)):
        if char == pattern[i]:

            # Label index replace
            s = list(label)
            s[i] = char
            label = "".join(s)

            # List insert
            usedChars.append(char)
            selectedAny = True

    # Fail message (is any letter selected?)
    if not selectedAny:
        print(f"No matches found for letter '{char}'")

