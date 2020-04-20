import math

def is_prime(num):
    # works great for small numbers
    # return num > 1 and not any(num % n == 0 for n in range(2,num))

    # hope this works for bigger numbers
    # Nope, it says that 4 is a prime ^^
    # if num == 1: return False
    # for i in range(2, int(num**0.5)):
    #     if num % i == 0: return False
    # return True

    # experiment 3
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    sq = int(math.sqrt(num))
    for x in range(3, sq+1,2):
        if num % x == 0:
            return False
    return True

n = int(input())
for i in range(n):
    # is_prime(int(input()))
    if is_prime(int(input())) == True: print('Prime')
    else: print('Not prime')

num = 66
sq = int(math.sqrt(num))
for x in range(3, sq+1,2):
    print(x)
    print(num%x)

print()
print(range(3, sq+1,2))
