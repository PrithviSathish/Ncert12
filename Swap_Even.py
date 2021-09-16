def SWAP_EVEN(Arr, n):

    i = 0
    while i < n:

        if i % 2 != 0:
            i += 1
        else:
            tmp = Arr[i]
            Arr[i] = Arr[i + 2]
            Arr[i + 2] =tmp
            i += 1

li = [10, 11, 20, 22, 30, 33, 40, 44]
SWAP_EVEN(li, len(li))
print(li)
