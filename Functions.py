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
	

'''
----------- Factorial -------------
x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))
u = int(input("Enter the third value: "))
v = int(input("Enter the fourth value: "))

z = (fact(x) + fact(y)) / (fact(u) + fact(v))
print(z)


------------ Sum of 2 numbers --------------

# For sum without arg
sum1()

# For sum with arg
x = int(input("Enter the first num: "))
y = int(input("Enter the second num: "))
sum(x + y)

# For sum without arg but with return type
c = sum3()
print(c)

# For sum with arg and return type
x = int(input("Enter the first num: "))
y = int(input("Enter the second num: "))
z = sum(x, y)
print(z)

'''

