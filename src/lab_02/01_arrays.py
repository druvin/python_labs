def min_max(a):
    if a:
        minimum,maximum = 10*100, -10**100
        for x in a:
            if x < minimum: minimum = x
            if x > maximum: maximum = x
        return minimum, maximum
    else: raise ValueError("Пустой список или кортеж.")
def unique_sorted(a):
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
    result = []
    for row in a:
        if isinstance(row, (list, tuple)):
            for i in row: result.append(i)
        else: raise TypeError(f"Ожидался list или tuple, получен {type(row).__name__}")
    return result
a = [3, -1, 5, 5, 0]
b = [-1, -1, 0, 2, 2]
c = [[1, 2], [3, 5, 9]]
print(min_max(a))
print(unique_sorted(b))
print(flatten(c))