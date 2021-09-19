def validator(string):
    conditions = []
    conditions.append(sum([1 for letter in string if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) >= 2)
    conditions.append(sum([1 for digit in string if digit in '0123456789']) >= 3)
    conditions.append(string.isalnum)
    conditions.append(sum([1 for i in string if string.count(i) > 1]) == 0)
    conditions.append(len(string) == 10)
    if all(conditions):
        return 'Valid'
    else:
        return 'Invalid'


print(validator('B1CDEF2354'))
print(validator('B1CD102354'))

# for _ in range(int(input())):
#     validator(input())
