print("number of characters in the file: ", len(open(input("Enter the file name: "), "r").read()))

# Alternate method - proposed by Abinav
print("number of characters in the file: ", open(input("Enter the file name: "), "a").tell())