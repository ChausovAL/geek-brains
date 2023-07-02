a = int(input("Введите первый элемент: "))
d = int(input("Введите шаг прогрессии: "))
progression_list = [a + (d * (i - 1)) for i in range(1, int(input("Введите количество элементов: ")) + 1)]
print(progression_list)
