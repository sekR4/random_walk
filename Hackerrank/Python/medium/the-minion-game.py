
# tribute goes to abitrolly who had the idea with counting back


def minion_game(string):
    kev, stu, s = [], [], string
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            kev.append(len(s)-i)
        else:
            stu.append(len(s)-i)

    if sum(kev) == sum(stu):
        print('Draw')
    elif sum(kev) > sum(stu):
        print(f'Kevin {sum(kev)}')
    else:
        print(f'Stuart {sum(stu)}')


if __name__ == '__main__':
    # s = input()
    s = 'BANANA'
    minion_game(s)
