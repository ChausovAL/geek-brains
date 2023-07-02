lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
lst2 = []
for i in lst1:
    if i >= 7 and i <= 10:
        lst2.append(lst1.index(i))
print(lst2)
