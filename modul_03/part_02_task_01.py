i = [1, 4, 6, 1, True, True, "hello", "a", 5, 'hello']
t = []
for x in i:
    if i.count(x) > 1 and t.count(x) == 0:
        t.append(x)
print(t)