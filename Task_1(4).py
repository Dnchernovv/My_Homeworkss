import sys

hours,salary_per_hour, bonus = map(float, sys.argv[1:])

print('Salary - {}'.format(hours * salary_per_hour + bonus))