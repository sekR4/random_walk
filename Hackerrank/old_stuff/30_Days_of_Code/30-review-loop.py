

# for n in range(int(input())):
#     string = input()
#
#     lst = [i for i in string]
#
#     first = ''
#     last = ''
#     for i in range(len(lst)):
#         if i%2==0:
#             first += lst[i]
#         else:
#             last += lst[i]
#
#     print(first,last)

#best solution
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
