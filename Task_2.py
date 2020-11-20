n = int(input())
hours = (n % 86400) // 3600
minutes = (n % 1440) // 60
seconds = ((n % 86400) % 60)
minutes1 = str(minutes)
seconds1 = str(seconds)
hours1 = str(hours)
print(hours1.zfill(2),minutes1.zfill(2),seconds1.zfill(2), sep=':')