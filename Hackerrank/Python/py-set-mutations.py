_, A = input(), set(map(int, input().split()))
for i in range(int(input())):  # N
    #       A.      command                       (B)
    eval(f'A.{input().split()[0]}({set(map(int,input().split()))})')
print(sum(A))


# cmd, _ = input().split()
# B = set(input().split())
# print(A)
# print(cmd)
# print(B)
#
# A.symmetric_difference(B)
#
# print(A)


# N = int(input())
#
# for i in range(N):
#     cmd, _ = input().split()
#     B = set(input().split())
#     print(f'A.{cmd}(B)')
#     result = eval(f'A.{cmd}(B)')
#     print(result)
#     eval(f'A.{cmd}(B)')
#     # eval('s.{0}({1})'.format(*input().split()+['']))
#
# print(len(A))

# n = int(input()) A = set(map(int,input().split())) c = int(input())
# for i in range(0,c):
#     eval('A.{0}({2})'.format(*input().split(),set(map(int,input().split()))))
# print(sum(A))
