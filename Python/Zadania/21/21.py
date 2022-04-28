# Def
def nwd(n1:int, n2:int):
    if n1 % n2 == 0:
        return n2
    else:
        return nwd(n2, (n1 % n2))
### Logic
num1 = int(input("Give first number: "))
num2 = int(input("Give second number: "))
print(f"The largest common divider for numbers {num1} and {num2} is {nwd(num1, num2)}")
