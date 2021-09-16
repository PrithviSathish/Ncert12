n_li = [["bot", "newbot"], [1, "hi"], [2, "bye"], [3, "die"]]
for i in n_li:
    for j in i:
        if j != 2:
            continue
        elif j == 2:
            print(i)
