
for i in range(int(input())):
    print(''.join([f'{i+1}' for i in list(range(i+1))]) +
          ''.join(sorted([f'{i}' for i in list(range(i+1)) if i > 0],
                         reverse=True)))

# lol...?
for i in range(0, int(input())):
    print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321,
           123456787654321, 12345678987654321, 12345678910987654321][i])
