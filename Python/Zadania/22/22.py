# Import
import random

### Preparation

password = ""
distincted = []

# Input
length = int(input("Type the length of generated password: "))
cmd = input("Shall the letters be used only?[y/N]: ").lower()
useLets = (cmd == 'y')

cmd = input("Distincted characters ('--' to end):\n").lower()
while not cmd == '--':
    if len(cmd) == 1:
        distincted.append(ord(cmd.upper()))
    else:
        print(f"'{cmd}' is not a single character!")
    cmd = input()

if useLets:
    charRange = range(65, 91)
else:
    charRange = range(33, 127)

### Logic
for i in range(0, length):
    # Randomize
    charId = random.choice(charRange)
    while charId in distincted:
        charId = random.choice(charRange)
    char = chr(charId)

    # Size
    if random.choice([0, 1]) == 1:
        char = char.lower()
    
    # Append
    password += char

# Output
print(f"Generated password:\n{password}")
