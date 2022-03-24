a = float(input("Podaj pierwsza liczbę 'a' : "))
b = float(input("Podaj drugą liczbę 'b' : "))
result = 0

arg = input("Co chcesz zrobic?:\n '+' - dodaj\n '-' - odejmij\n '*' - przemnóż\n '/' - podziel\n")

if arg == '+':
    result = a + b
elif arg == '-':
    result = a - b
elif arg == '*':
    result = a * b
else:
    if b != 0:
        result = a / b
    else:
        print("Pamietaj cholero - NIGDY nie dziel przez zero!")
        exit()

print(">> ", a, " ", arg, " ", b, " = ", result)