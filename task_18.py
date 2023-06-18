n = int(input("Введите количество элементов в массиве N: "))
list_1 = []
for i in range(n):
    n1 = int(input("Введите число: "))
    list_1.append(n1)
x = int(input("Введите число X: "))
dict_1 = {}
list_2 = []
if max(list_1) <= x:
    print(f"Близкий по величине элемент к заданному числу X: {max(list_1)}")
elif x in list_1:
    print(f"Число {x} находится в массиве")
else:
    for j in list_1:
        if x - j > 0:
            dict_1[x - j] = j
            list_2.append(x - j)
    print(f"Близкий по величине элемент к заданному числу X: {dict_1[min(list_2)]}")



