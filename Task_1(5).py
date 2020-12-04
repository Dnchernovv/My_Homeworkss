with open('meow_file.txt','w') as meowing:
    while True:
        user_input = input('Enter something: ')
        if user_input == '':
            break
        meowing.write(user_input + '\n')
