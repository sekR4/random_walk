
import re

# my solution (working)
# for i in range(int(input())):
#     sample = input()
#
#     m1 = re.match('^7|8|9',sample)
#     m2 = re.match('^[0-9]*$',sample)
#
#     if m1 and m2 and len(sample) == 10:
#         print('YES')
#     else:
#         print('NO')

# best practice
for i in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):
        print('YES')
    else:
        print('NO')
