# Variant 1
month = int(input('Enter a month number: '))
times = ['winter','spring','summer','autumn']
if month >= 1 and month < 3 or month == 12:
    print('This is {}'.format(times[0]))
elif month >= 3 and month < 6:
    print('This is {}'.format(times[1]))
elif month >= 6 and month < 9:
    print('This is {}'.format(times[2]))
elif month >= 9 and month < 12:
    print('This is {}'.format(times[3]))

# Variant 2
month = int(input('Enter a month number: '))
times = {'winter':[1,2,12],'spring':[3,4,5],'summer':[6,7,8],'autumn':[9,10,11]}
if month in times['winter']:
    print('This is winter')
elif month in times['spring']:
    print('This is spring')
elif month in times['summer']:
    print('This is summer')
elif month in times['autumn']:
    print('This is autumn')

