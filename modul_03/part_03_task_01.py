from math import sqrt
def area(a, b, c):
    p2 = 0.5 * (a + b + c)
    s = sqrt(p2 * (p2 - a) * (p2 - b) * (p2 - c))
    if s == 0 or a <= 0 or b <= 0 or c <=0:
        return('Вы ввели не правильные значения сторон')
    else:
        return(s)

a = int(input('1 сторона'))
b = int(input('2 сторона'))
c = int(input('3 сторона'))

print(area(a, b, c))
