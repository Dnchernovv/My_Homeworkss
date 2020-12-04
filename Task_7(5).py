from statistics import mean
import json
slr_r = open('firms.txt',encoding='utf8')
firms = slr_r.readlines()
firm_names = []
profits = []
f_1,f_2,f_3 = firms
p_1 = [int(x) for x in f_1.split() if x.isdigit()]
p_2 = [int(x) for x in f_2.split() if x.isdigit()]
p_3 = [int(x) for x in f_3.split() if x.isdigit()]
for j in [p_1,p_2,p_3]:
    profits.append(j[0]-j[1])
for i in firms:
    firm_names.append(i[0:i.find('_')+2])
r_profits = [x for x in profits if x > 0]
print(f'Средняя прибыль равняется {mean(r_profits)}')
for x in profits:
    if x > 0:
        print(f'Прибыль {profits.index(x)+1}-ой фирмы равна {x}')
average = {'Average':(mean(profits))}
firms_profits = dict(zip(firm_names,profits))
firms_profits = [firms_profits,average]
print(firms_profits)
with open('firms.json','w') as write_j:
    json.dump(firms_profits,write_j)

