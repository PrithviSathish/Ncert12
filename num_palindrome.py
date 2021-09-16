n = int(input("Enter the number: "))
n1 = n
a = 0
while n > 0:
    v = 10 ** (len(str(n)) - 1)
    a += (n % 10) * v
    n //= 10

if a == n1:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
