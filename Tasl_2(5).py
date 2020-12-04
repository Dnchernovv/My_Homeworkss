f_object = open('my_file.txt')
a  = f_object.readlines()
print(len(a))
for i in a:
    print(f'Строка {a.index(i)+1} содержит {len(i.split())} слов')
f_object.close()