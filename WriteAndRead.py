f = open(input("Enter the file to be created: "), 'w+')
f.write(input("Enter the contents: "))

print(f.read())
f.close()
