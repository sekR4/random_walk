# a, b, m = int(input()), int(input()), int(input())
a, b, m = [int(input()) for _ in '123']  # krass, ich kann ne liste so einfach aufloesen
print(pow(a, b), pow(a, b, m), sep='\n')
