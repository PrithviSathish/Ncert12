# Factorial
def fact(n):
    f1 = 1
    for i in range(1, n + 1):
        f1 *= i
    return f1


# Without arg
def sum1():
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    c = a + b
    print(c)


# With arg
def sum2(a, b):
    print(a + b)


# Without arg but with return type
def sum3():
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    return a + b


# With arg and return type
def sum2(a, b):
    return a + b


# subtract with return
def diff(a, b):
    return a - b


# sum of n numbers without return
def sum_natural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("sum of first", n, "natural numbers is:", sum)

# Find the mean of the list
def myMean(l):
    s = 0
    for x in l:
        s += x
    return s / len(l)
