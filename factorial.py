Number = int(input("Enter the number: "))
n, result = Number, 1

while n:
    result = result * n
    n = n - 1

factorial = result 
print("Factorial of ", Number, "is", factorial)