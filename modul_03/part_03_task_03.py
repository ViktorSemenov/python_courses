
def max_number(b):
    from itertools import permutations
    b = list(permutations(b))
    a1 = []
    for i in b:
        v = list(map(str, i))
        c = ''.join(v)
        a1.append(int(c))
    print(max(a1))

a = [97867, 8, 873, 86, 91, 919]
b = [234, 1000, 919, 7, 9, 78]
max_number(a)
max_number(b)