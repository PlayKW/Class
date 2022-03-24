import random

t = ["papier", "kamień", "nożyce"]
bot = ""
player = ""
botP = 0
playerP = 0

while botP < 3 and playerP < 3:
    bot = random.choice(t)
    player = input("Co dajesz?(kamień/papier/nożyce): ")
    if player in t:
        if bot == player:
            playerP += 0
        elif bot == "kamień":
            if player == "papier":
                playerP += 1
            else:
                botP += 1
        elif bot == "papier":
            if player == "nożyce":
                playerP += 1
            else:
                botP+= 1
        else:
            if player == "kamień":
                playerP += 1
            else:
                botP += 1

        print(f"{player} - {bot}: {playerP} - {botP}")
    else:
        print("Nie ma takiej opcji :(!")

if playerP == 3:
    print(f"WYGRYWASZ! ({playerP} - {botP})")
else:
    print(f"PRZEGRYWASZ! ({playerP} - {botP})")
