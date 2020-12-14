n_cases = 2


n = 6
sides = [4, 3, 2, 1, 3, 4]
# 3
sides = [1, 3, 2]
# print(*reversed(sides))
print(sides)
print(sides[0] > sides[1] or sides[len(sides)-1] > sides[len(sides)-2])

print(sides[::-1])

# for _ in range(int(input())):
#     _ = input()
#     sides = list(map(int, input().split()))
#     if sides[0] > sides[1] or sides[len(sides)-1] > sides[len(sides)-2]:
#         print('Yes')
#     else:
#         print('No')

for _ in range(int(input())):
    n = input()
    sides = list(map(int, input().split()))
    if sides[0] > sides[1] or sides[len(sides)-1] > sides[len(sides)-2]:
        print('Yes')
    else:
        print('No')
