some_words = str(input('Enter a phrase: '))
some_list = some_words.split()
for i in some_list:
    if len(i)>10:
        print('{} is {}'.format(some_list.index(i)+1,i[:10]))
    else:
        print('{} is {}'.format(some_list.index(i)+1,i))