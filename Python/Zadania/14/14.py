import random

tab = random.sample(range(1,51), 6)
sh = []
shR = []
p = 0
n = 0

while(n < 6):
    inp = int(input(f"{sh}: "))
    if inp in range(1,51):
        sh.append(inp)
        n+=1
    else:
        print(f"Liczba {inp} jest poza zakresem 1-50")

for get in sh:
    if get in tab:
        p += 1
        shR.append(get)



if p == 1:
    print(f"{sh} Trafiłeś 1 liczbę: {shR}")
else:
    print(f"{sh} Trafiłeś {p} liczb: {shR}")
