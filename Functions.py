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
def sum4(a, b):
    return a + b


# subtract with return
def diff(a, b):
    return a - b


# sum of n numbers without return
def sum_natural(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    print("sum of first", n, "natural numbers is:", s)


# Find the mean of the list
def myMean(li):
    s = 0
    for x in li:
        s += x
    return s / len(li)


# Change a string
def string(s):
    print("Original String:", s)
    s = "Welcome"
    print("New string:", s)


# Change a tuple
def change_tup(tu):
    tu2 = tu
    tu = ()
    for i in tu2:
        if i <= 60:
            tu += (i + 5,)
        else:
            tu += (i,)

    print("In the function:", tu)


# volume of a cuboid
def vol_cub(l=3, b=6, h=20):
    print(l, b, h)
    return l * b * h


# name of a person
def full_name(first, last):
    print(first, last)


def globe_value(x, y):
    global a
    x, y = y, x
    b = 30
    c = b + b
    print(a, c, x, y)

