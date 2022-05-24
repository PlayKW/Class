# Import
import math

# Def
def numLvl(num:float):
    if a > 0:
        print(f"{a} jest dodatnia")
    elif a < 0:
        print(f"{a} jest ujemna")
    else:
        print(f"{a} jest równa 0")

def canDiv(num:float, div:float):
    if num % div == 0:
        print(f"{num} jest podzielna przez {div}")
    else:
        print(f"{num} nie jest podzielna przez {div}")

def absolute(num):
    return math.sqrt(num**2)

# Input
print("1 - Kalkulator\n2 - Kalkulator objętości\n3 - Info o liczbie")
cmd = input("Wybierz operację: ")

### Logic
# Calculator
if cmd == '1' : 
    a = float(input("Podaj pierwsza liczbę 'a' : "))
    b = float(input("Podaj drugą liczbę 'b' : "))
    result = 0

    arg = input("Co chcesz zrobic?:\n '+' - dodaj\n '-' - odejmij\n '*' - przemnóż\n '/' - podziel\n '^' - podnieś do potęgi (a^b)\n 'hp' - hypot\n")

    if arg == '+':
        result = a + b
    elif arg == '-':
        result = a - b
    elif arg == '*':
        result = a * b
    elif arg == '/':
        if b != 0:
            result = a / b
        else:
            print("")
            exit()
    elif arg == '^':
        result = a ** b
    elif arg == "hp":
        result = math.hypot(a, b)
        print(">> hypot(", a, ", ", b, ") = ", result)
        exit()
    else:
        print("Polecenie '", arg, "' nie istnieje!")
        exit()

    print(">> ", a, " ", arg, " ", b, " = ", result)

# Value calculator
elif cmd == '2':
    cmd = input("Czego objętość liczymy?:\n 'sześcian' \n 'prostopadłościan' \n 'ostrosłup'\n")
    if cmd == 'sześcian':
        a = float(input("Podaj krawędź figury: "))
        if a >= 0:
            print(f"Objętość sześcianu o krawędzi {a} wynosi {a**3}")
        else:
            print("Liczba poza zakresem:  >= 0")
    elif cmd == 'prostopadłościan':
        a = float(input("Podaj krawędź podstawy: "))
        b = float(input("Podaj drugą krawędź podstawy: "))
        h = float(input("Podaj wysokość: "))
        if a >= 0 and b >= 0 and h >= 0:
            print(f"Objętość prostopadłościanu o krawędziach {a},{b} i {h} wynosi {a*b*h}")
        else:
            print("Liczba poza zakresem:  >= 0")
    elif cmd == 'ostrosłup':
        a = float(input("Podaj krawędź podstawy: "))
        b = float(input("Podaj drugą krawędź podstawy: "))
        h = float(input("Podaj wysokość: "))
        if a >= 0 and b >= 0 and h >= 0:
            print(f"Objętość ostrosłupa o krawędziach podstawy {a} i {b} oraz wysokości {h} wynosi {a*b*h/3}")
        else:
            print("Liczba poza zakresem:  >= 0")
    else:
        print(f"Polecenie '{cmd}' nie istnieje!")



# Num info
elif cmd == '3':
    a = float(input("Podaj liczbę: "))
    print(f"======- Info o liczbie {a} -======")
    numLvl(a)
    canDiv(a, 3)
    print(f"Wartość bezwzględna z {a} wynosi {absolute(a)}")

# Command deny
else:
    print(f"Polecenie '{cmd}' nie istnieje!")


