file = open("hash_file.txt", "r")
res = []
for x in file.readlines():
    res.append(x.split("#"))

for i in res:
    for j in i:
        print(j)
