x = float(input("Podaj pierwszą współrzędną(x): "))
y = float(input("Podaj pierwszą współrzędną(y): "))

p = f"{x}, {y}"

if x == 0:
    if y == 0:
        print(f"Punkt ({p}) jest dokładnie w środku układu współrzędnych")
    elif y > 0:
        print(f"Punkt ({p}) leży na osi Y między ćwiartką I, a II")
    else:
        print(f"Punkt ({p}) leży na osi Y między ćwiartką III, a IV")
elif y == 0:
    if x > 0:
        print(f"Punkt ({p}) leży na osi X między ćwiartką I, a IV")
    else:
        print(f"Punkt ({p}) leży na osi X między ćwiartką II, a III")
elif x > 0:
    if y > 0:
        print(f"Punkt ({p}) leży w I ćwiartce")
    else:
        print(f"Punkt ({p}) leży w IV ćwiartce")
elif x < 0:
    if y > 0:
        print(f"Punkt ({p}) leży w II ćwiartce")
    else:
        print(f"Punkt ({p}) leży w III ćwiartce")
else:
    print("Coś żeś Pan namiszoł.. :/")
