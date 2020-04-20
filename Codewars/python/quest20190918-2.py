# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

# for example, a tower of 3 floors looks like below
#
# [
#   '  *..',
#   ' ***.',
#   '*****'
# ]

# tower_builder(3) -> ['  *  ', ' *** ', '*****']

floors = 3
# if floors > 1:
#     print((floors + (floors - 1)) * '*')
#
# if floors > 1:
#     print((floors + (floors - 3))*'*')

def tower_builder(floors):
    # brackets = []
    brackets2 = []
    for i in range(floors):
        # print((floors - (i+1))*' '+ (i+1)*'*' + (floors - (i+1))*' ')
        #brackets.append((floors - (i+1))*' '+ (i+1)*'*' + (floors - (i+1))*' ')
        # brackets.append((floors - (i+1))*'.'+ (i+1)*'*' + (floors - (i+1))*'.')
        brackets2.append((floors - (i+1))*' '+ (i*2+1)*'*' + (floors - (i+1))*' ')
    # print(brackets)
    print(brackets2)


def tower_builder(n_floors):
    return [(n_floors - (i+1))*' '+ (i*2+1)*'*' + (n_floors - (i+1))*' ' for i in range(n_floors)]

def tower_builder(n): # best practice
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
tower_builder(3)

print('haha'.center(2))
