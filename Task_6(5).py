my_dict = dict()
with open('classes.txt',encoding='utf-8') as class_info:
     classes = class_info.readlines()
for line in classes:
    splitted_line = line.split()
    subject = splitted_line[0]
    sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_lessons
print(my_dict)