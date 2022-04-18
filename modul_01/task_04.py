x1 = float(input('Укажите первое число: '))
x2 = float(input('Укажите второе число: '))
x3 = float(input('Укажите третье число: '))

if x1 == x2 and x2 == x3:
    print('Выявлено 3 совпадения')
elif x1 == x2 or x2 == x3 or x1 == x3:
    print('Выявлено 2 совпадений')
else:
    print('Выявлено 0 совпадения')