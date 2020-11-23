start_km = 2
finish = 3
days = 1
while start_km < finish:
    start_km *= 1.1
    print('{}-й день: {}'.format(days,round(start_km,2)))
    days += 1
print('Спротсмен добьется результата за {} дней'.format(days))