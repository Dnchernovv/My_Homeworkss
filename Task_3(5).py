from statistics import mean
salary = open('salaries.txt',encoding='utf-8')
salaries = salary.read().split()
surnames = []
salary = []
for i in range(0,len(salaries)):
    if i % 2 == 0:
        surnames.append(salaries[i])
    elif i % 2 != 0:
        salary.append(salaries[i])
salary = list(map(lambda x: int(x), salary))
info = dict(zip(surnames,salary))
print('Следующие сотрудники имеют зарплату более 20 тыс. руб. в месяц: ')
for key,value in info.items():
    if value > 20000:
        print(f'Зарплата {key} равна {value} рублей')
print(f'Средняя зарплата равна {mean(salary)}')

