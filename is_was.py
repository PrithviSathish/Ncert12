file = open("sample.txt", "r")
num_is, num_was = 0, 0
for line in file.readlines():
    words = line.split(" ")

for i in words:
    if i.lower() == "is":
        num_is += 1
    if i.lower() == "was":
        num_was += 1

print(f"Number of 'is' characters: {num_is}\nNumber of 'was' characters: {num_was}")

