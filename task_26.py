def exponentiation(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * exponentiation(a, b - 1))
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(exponentiation(a, b))
