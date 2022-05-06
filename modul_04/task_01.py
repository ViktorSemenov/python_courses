def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1


a = [i for i in range(1, 100, 2)]
print(a)
b = int(input('Введите число для поиска '))
print('Индекс вашего числа в массиве', binary_search(a, b))