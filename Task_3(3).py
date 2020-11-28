def maximizer(arg_1,arg_2,arg_3):
    my_list = [arg_1,arg_2,arg_3]
    for x in range(len(my_list)):
        if my_list[x] == min(my_list):
            my_list.pop(x)
            break
    return sum(my_list)
print(maximizer(10,100,1))