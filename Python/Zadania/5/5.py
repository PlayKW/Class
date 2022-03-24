from tokenize import Double


a = float(input("Podaj bok 'a': "))
b = float(input("Podaj bok 'b': "))
c = float(input("Podaj bok 'c': "))

if a==0 or b==0 or c==0:
    print("Nie da sie zbudować takiego trójkąta!")
elif a+b<=c or b+c<=a or c+a<=b:
    print("Nie da sie zbudować takiego trójkąta!")
else:
    print("Ten trójkąt jest możliwy.")