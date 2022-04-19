x = float(input('Введите начальную сумму'))
y = float(input('Введите сумму которую хотите получить'))
p = float(input('Введите процент вклада'))
t = 0
while x < y:
    a = x * p / 100
    x += a
    x = int(x)
    print(x, a)
    t +=1

print("Срок вклада {0} лет".format(t))
