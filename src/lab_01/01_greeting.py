name = input('Введите свое имя: ')
age = input('Введите свой возраст: ')
if not age.isdigit():
    print('Введите свой возраст!')
else:
    print(f'Привет, {name}! Через год тебе будет {int(age) + 1}.')