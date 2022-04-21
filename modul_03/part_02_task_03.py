d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
k = []
v = []
d2 = {}
for i in d:
    k.append(i)
    v.append(d[i])

for i in range(len(k)):
    d2[v[i]] = k[i]
d = d2
print(d)