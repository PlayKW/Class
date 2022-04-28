# Def
def nextFib(n1: int, n2:int, itr:int, c:int):
    if itr < c:
        itr += 1
        print(n1)
        nextFib(n1+n2, n1, itr, c)

### Logic
# Input
count = int(input("How many numbers from the Fibbonacci's sequence should be printed?: "))
# Loop
if count >= 0:
    nextFib(1, 0, 0, count)
else:
    print("Have you ever counted backwards?")