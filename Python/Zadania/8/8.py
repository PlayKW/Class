import random

min = int(input("Podaj najmnijszą mozliwa liczbę: "))
max = int(input("Podaj największą mozliwa liczbę: "))

for x in range (1,6):
    print(random.randint(min,max))