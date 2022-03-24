#import
import random

#preparation
wrds = []
for x in range(1,21):
    wrds.append(f"slowko{x}")

pattern = random.choice(wrds)
screen = ""

for c in pattern:
    screen += '-'

#display