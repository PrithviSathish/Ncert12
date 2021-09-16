Num = int(input("Enter the number: "))
print("The Fibonacci series: ")
Num1 = -1
Num2 = 1
Num3 = Num1 + Num2
print(Num3, end=' ')

for i in range(1, Num):
    Num1 = Num2
    Num2 = Num3
    Num3 = Num1 + Num2
    print(Num3, end=' ')

print()