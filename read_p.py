in_file = open("test.txt", "r")
out_file = open("out.txt", "w")
for line in in_file.readlines():
    if line=="":
        continue
    else:
        if line.lower().startswith('p'):
            out_file.write(line)

in_file.close()
out_file.close()
print("completed successfully")
