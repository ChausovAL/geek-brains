x = input("Введите слово: ")

data = {"AEIOULNSTRАВЕИНОРСТ": 1,
        "DGДКЛМПУ": 2,
        "BCMPБГЁЬЯ": 3,
        "FHVWYЙЫ": 4,
        "KЖЗХЦЧ": 5,
        "JXШЭЮ": 8,
        "QZФЩЪ": 10
}
count = 0
for i in x.upper():
    for j in data.keys():
        if i in j:
            count += data[j]

print(count)