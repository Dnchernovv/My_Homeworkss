# variant 1
def my_func(x,y):
    return x**y
print(my_func(2,-2))
# variant 2
def my_func2(x, y):
    while y < 0:
        y += 1
        x = 1 / x * 1 / x
        return x
print(my_func2(2,-2))