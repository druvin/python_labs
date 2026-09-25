def min_max(a):
    """Возвращает кортеж (минимум, максимум) без использования встроенных min() и max()."""
    if a:
        minimum,maximum = 10*100, -10**100
        for x in a:
            if x < minimum: minimum = x
            if x > maximum: maximum = x
        return minimum, maximum
    else: raise ValueError("Пустой список или кортеж.")
def unique_sorted(a):
    """Возвращает отсортированный список уникальных элементов без sort() и sorted()."""
    uniq = []
    for x in a:
        if x not in uniq: uniq.append(x)
    c = len(uniq)
    for i in range(c):
        for j in range(0, c - i - 1):
            if uniq[j] > uniq[j + 1]:
                uniq[j], uniq[j + 1] = uniq[j + 1], uniq[j]
    return uniq
def flatten(a):
    """«Расплющивает» список списков/кортежей в один одномерный список."""
    result = []
    for row in a:
        if isinstance(row, (list, tuple)):
            for i in row: result.append(i)
        else: raise TypeError(f"Ожидался list или tuple, получен {type(row).__name__}")
    return result
a = [[3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]
for i in a: 
    try:
        print(f'{i} -> {min_max(i)}')
    except ValueError: print(f'{i} -> ValueError')
b = [[3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]]
for i in b: print(unique_sorted(i))
c = [[[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"]
]
for i in c: 
    try:
        print(f'{i} -> {flatten(i)}')
    except TypeError: print(f'{i} -> TypeError')
