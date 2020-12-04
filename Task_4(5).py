numbers_english = open('nums.txt', 'r', encoding='utf-8')
a = numbers_english.readlines()
with open('russian.txt','w', encoding='utf-8') as numbers_russian:
    for i in range(len(a)):
        if 'One' in a[i]:
            a[i] = a[i].replace('One','Один')
            numbers_russian.write(a[i])
        elif 'Two' in a[i]:
            a[i] = a[i].replace('Two','Два')
            numbers_russian.write(a[i])
        elif 'Three' in a[i]:
            a[i] = a[i].replace('Three','Три')
            numbers_russian.write(a[i])
        elif 'Four' in a[i]:
            a[i] = a[i].replace('Four','Четыре')
            numbers_russian.write(a[i])

numbers_english.close()
