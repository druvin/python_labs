name = input('Введите ваше ФИО: ').split(' ')
full_name_mas = [i for i in name if i]
initials = ''
full_name = ''
length = 0
for i in full_name_mas:
    initials = i[0] + initials
    length += len(i)
    full_name = full_name + i + ' '
print(f'ФИО: {full_name}')
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length+2}')