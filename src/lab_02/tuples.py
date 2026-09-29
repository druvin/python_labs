def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует данные студента в строку вида 'Фамилия И.О., гр. ГРУППА, GPA X.XX'"""
    if not isinstance(rec, tuple):
        raise TypeError("Введен не кортеж")
    if len(rec) != 3:
        raise ValueError("Длина кортежа должна быть 3")
    name, group, gpa = rec
    if not isinstance(name, str) or not isinstance(group, str) or not isinstance(gpa, (int, float)):
        raise TypeError("Тип данных не соответствует ожидаемому")
    fio = name.split()
    if len(fio) not in (2,3):
        raise ValueError("Неверно указаны данные")
    if not group.strip():
        raise ValueError("Пустая гурппа")
    if not (0 <= gpa <= 5):
        raise ValueError("Неверно указан GPA")
    surname = fio[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in fio[1:])
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
a = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
("Петров Пётр", "IKBO-12", 5.0),
("Петров Пётр Петрович", "IKBO-12", 5.0),
("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
]
for i in a:
    try:
        print(f'{i} -> {format_record(i)}')
    except ValueError: print(f'{i} -> ValueError')
    except TypeError: print(f'{i} -> TypeError')