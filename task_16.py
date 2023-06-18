n = int(input("Введите количество элементов в массиве N: "))
list_1 = []
for i in range(n):
    n1 = int(input("Введите число: "))
    list_1.append(n1)
x = int(input("Введите число X: "))
count = 0
for j in list_1:
    if j == x:
        count += 1
print(f"Число {x} в массиве встречается в количестве: {count}")