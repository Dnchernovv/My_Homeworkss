# Variant 1
from itertools import cycle,count
point = int(input('Enter a starting point: '))
for el in count(start = point):
    print(el)
    if el > 1000:
        break
# Variant 2
x = 5
race = ['ready','set','go!','finish!']
for stage in cycle(race):
    x -= 1
    print(stage)
    if x < 0:
        break