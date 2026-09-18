n1,n2 = input('Введите первое число: ').replace(',','.'), input('Введите второе число: ').replace(',','.')
print(f'sum={(float(n1)+float(n2)):.2f}; avg={((float(n1)+float(n2))/2):.2f}')