my_list = list(input('Enter something: '))
for x in range(1,len(my_list),2):
    my_list[x],my_list[x-1] = my_list[x-1],my_list[x]
print(my_list)