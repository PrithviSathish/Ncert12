# Counting all characters in file
# print("number of characters in the file: ", len(open(input("Enter the file name: "), "r").read()))

# Alternate method - proposed by Abinav
# print("number of characters in the file: ", open(input("Enter the file name: "), "a").tell())

# counting induvidual characters
f = open(input("Enter the file name: "), 'r')
out = {"Alphabet" : 0, "Upper" : 0, "Lower" : 0, "Numeric" : 0, "Space" : 0, "Special" : 0}
for char in f.read():
    if char.isalpha():
        out['Alphabet'] += 1
    if char.isupper():
        out['Upper'] += 1
    if char.islower():
        out['Lower'] += 1
    elif char.isnumeric():
        out["Numeric"] += 1
    elif char.isspace():
        out["Space"] += 1
    else:
        out["Special"] += 1

for key, value in out.items():
    print(key, value)
