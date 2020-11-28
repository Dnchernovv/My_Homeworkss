def my_div(x,y):
    try:
        x, y = int(x),int(y)
        div = x/y
        return div
    except ZeroDivisionError:
        return 'Pick another number'
    except ValueError:
        return 'Should be a number'

print(my_div(input(),input()))