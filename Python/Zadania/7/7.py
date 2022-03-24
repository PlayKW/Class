import math

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
        print("Pamietaj cholero - NIGDY nie dziel przez zero!")
        exit()
elif arg == '^':
    result = a ** b
elif arg == "hp":
    result = math.hypot(a, b)
    print(">> hypot(", a, ", ", b, ") = ", result)
    exit()
else:
    print("Opcja '", arg, "' nie istnieje!")
    exit()

print(">> ", a, " ", arg, " ", b, " = ", result)