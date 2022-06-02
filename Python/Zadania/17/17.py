# Import
import random

# Lista jest pusta, bo na dole zostanie wygenerowane 20 kolejnych słów.
# Można tą pętlę usunąć i wypisać w liście słowa - też będzie działać.
# Przykładowa lista : ["komputer","python","programowanie","algorytm","skrypt","składnia","obkiekt","monitor","zasilacz","kamera","procesor","pamięć ram","słuchawki","mysz","karta graficzna","wentylator","pendrive","dysk","płyta","chmura"]

### Preparation
wrds = [str]
usedChars = []

for x in range(1,21):
    wrds.append(f"slowko{x}")


pattern = random.choice(wrds).lower()
label = ""
tries = 0

for c in pattern:
    if not c == ' ':
        label += '-'
    else:
        label += ' '

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
    inp = input("Question: ").lower()
    if inp in usedChars:
            print(f"You have already asked about this letter!")
            continue

    # Letter select
    if len(inp) == 1:

        # List insert
        usedChars.append(inp)

        # Is lettern in a pattern?
        if inp in pattern:

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
            print(f"Word '{inp}' is incorrect!")

### End
print(ftr)
print("Congratulations!")
print(f"The chosen word was '{pattern}'.")
print(f"It took you {tries} tries to guess it!")
