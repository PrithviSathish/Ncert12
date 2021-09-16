x = int(input('Enter the value of x: '))
n = int(input('Enter the value of n: '))
Sum = 0
for i in range(0, n):
    faci = 1
    for j in range(1, i * 3 + 2):
        faci *= j
    Sum = Sum + 1 / faci - ((i % 2) * 2 / faci)
Sum *= x
print(Sum)