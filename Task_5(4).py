from functools import reduce
def mult(x,y):
    return x * y
my_numbers = [x for x in range(100,1001)]
my_numbers = reduce(mult,my_numbers)

print(my_numbers)