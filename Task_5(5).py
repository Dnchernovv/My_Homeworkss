from functools import reduce
with open ('numbers2.txt','x+') as f_nums:
    f_nums.write('1 2 3 4 5')
with open ('numbers2.txt','r') as f_nums2:
    nums = f_nums2.readline()
    nums = nums.split()
    nums = list(map(lambda x: int(x),nums))
    print(sum(nums))

