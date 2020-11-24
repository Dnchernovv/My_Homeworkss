my_list = [7,5,3,3,2]
new_elem = int(input('Введите новое число: '))
for x in my_list:
    if new_elem in my_list:
        if new_elem == x:
            my_list.insert(my_list.index(x),new_elem)
            break
    else:
        my_list.append(new_elem)
        break
print(my_list)