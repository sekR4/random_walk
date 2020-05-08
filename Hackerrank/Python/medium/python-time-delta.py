import datetime

# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone.

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

# print(datetime.date(t1))

print(datetime.datetime.strptime(t1, '%a %d %B %Y %H:%M:%S %z'))

t1 = datetime.datetime.strptime(t1, '%a %d %B %Y %H:%M:%S %z')
t2 = datetime.datetime.strptime(t2, '%a %d %B %Y %H:%M:%S %z')

delta = t1-t2
print(int(delta.total_seconds()))

for _ in range(int(input())):
    delta = datetime.datetime.strptime(input(), '%a %d %B %Y %H:%M:%S %z') - \
        datetime.datetime.strptime(input(), '%a %d %B %Y %H:%M:%S %z')
    print(int(delta.total_seconds()))
