x = input('Введите пароль:\n')
while len(x) < 8 or x.islower() or x.isupper():
    x = input('Пароль не соответствует условиям\n')
else: print('Пароль принят')