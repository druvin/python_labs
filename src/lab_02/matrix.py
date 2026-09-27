def check_rectangle(mat: list[list[float | int]]) -> None:
    """Проверяет, что матрица прямоугольная. Пустая матрица — корректна."""
    if not mat: return []
    len_colons = len(mat[0])
    for row in mat:
        if len(row) != len_colons:
            raise ValueError("Матрица не прямоугольная (рваная)")

def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    '''Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError.'''
    check_rectangle(mat)
    if not mat: return []
    len_lines = len(mat)
    len_colons = len(mat[0])
    res = []
    for i in range(len_colons):
        new_row = []
        for j in range(len_lines):
            new_row.append(mat[j][i])
        res.append(new_row)
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке матрицы"""
    check_rectangle(mat)
    if not mat: return []
    res = []
    for row in mat:
        res.append(sum(row))
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    check_rectangle(mat)
    if not mat: return []
    colons = len(mat[0])
    res = []
    for i in range(colons):
        total = 0
        for row in mat:
            total += row[i]
        res.append(total)
    return res

a = [[[1, 2, 3]],
        [[1], [2], [3]],
        [[1, 2], [3, 4]],
        [],
        [[1, 2], [3]],
    ]
b = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]
c = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]
for i in a:
    try: print(f'{i} -> {transpose(i)}')
    except ValueError: print(f'{i} -> ValueError')
for i in b:
    try: print(f'{i} -> {row_sums(i)}')
    except ValueError: print(f'{i} -> ValueError')
for i in c:
    try: print(f'{i} -> {col_sums(i)}')
    except ValueError: print(f'{i} -> ValueError')