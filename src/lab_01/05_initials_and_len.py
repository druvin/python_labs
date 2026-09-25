name = input('Введите ваше ФИО: ').split(' ')
full_name_list = [i for i in name if i]
initials = ''
full_name =''
length = 0
for i in full_name_list:
    initials += i[0].upper()
    length += len(i)
    full_name += i + ' '
full_name = full_name.strip()
print(f'ФИО: {full_name}')
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {length+len(full_name_list) - 1}')