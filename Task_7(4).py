from math import factorial
from itertools import count

def fact():
    for f_num in count(1):
        yield factorial(f_num)
x = 1
for i in fact():
    print('Factorial of {} equals {}'.format(x, i))
    if x == 15:
        break
    x += 1
