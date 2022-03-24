import random

print("Zgadnij wylosowaną liczbę [1-20]")

goal = random.randint(1,20)
num = int(input("Podaj liczbę: "))
tries = 1

while num != goal:
    if num > goal:
        print(f"[>] Liczba {num} jest większa od wylosowanej")
    else:
        print(f"[<] Liczba {num} jest mniejsza od wylosowanej")
    
    num = int(input("Podaj liczbę: "))
    tries += 1

print(f"Brawo, wylosowana liczba to {goal}! Zgadłeś za {tries} razem.")
