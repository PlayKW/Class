# Input
count = int(input("How many numbers from the Fibbonacci's sequence should be printed?: "))
num = 1
pre_num = 0
backup = 0
# Loop
if count >= 0:
    for i in range(0, count):
        print(num)
        backup = num
        num += pre_num
        pre_num = backup
else:
    print("Have you ever counted backwards?")