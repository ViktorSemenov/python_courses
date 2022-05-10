
def maks_massiv(a):
    maksmas = a[0]
    maksmas_index = 0
    for i in range(len(a)):
        if a[i] > maksmas:
            maksmas = a[i]
            maksmas_index = i
    return maksmas_index

def selection_sort(a):
    newmas = []
    for i in range(len(a)):
        maksmas = maks_massiv(a)
        newmas.append(a.pop(maksmas))
    return newmas

a = [i for i in range(1, 100, 5)]
print(a)
print(selection_sort(a))
