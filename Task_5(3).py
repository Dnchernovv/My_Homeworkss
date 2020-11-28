def string():
    rule = False
    exec_sum = 0
    while rule == False:
        input_numbers = input('Enter a set of numbers of q to stop execution: ').split()
        result = 0
        for num in input_numbers:
            if 'q' in num:
                rule = True
                break
            result += int(num)
        exec_sum += result
    return exec_sum

print(string())