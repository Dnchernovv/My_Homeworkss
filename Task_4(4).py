redundant = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
clear = [x for x in redundant if redundant.count(x) == 1]
print(clear)
