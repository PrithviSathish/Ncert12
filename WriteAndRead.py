f = open(input("Enter the file to be created: "), 'w+', newline="\n")
content = input("Enter the contents: ")
f.write(content)
f.seek(0)
print(f.read())
f.close()
