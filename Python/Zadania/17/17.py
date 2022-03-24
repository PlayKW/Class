#import
import random

#preparation
wrds = []
usedChars = []
for x in range(1,21):
    wrds.append(f"slowko{x}")

pattern = random.choice(wrds)
screen = ""

for c in pattern:
    screen += '-'

#display
print("*======================*\n")
print(screen)
print(f"Used: {usedChars}")
