for i in range(int(input())):
    _, A, _, B = input(), set(input().split()), input(), set(input().split())
    print(A.issubset(B))
