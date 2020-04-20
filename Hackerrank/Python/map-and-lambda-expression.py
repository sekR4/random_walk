# numbers = [1, 2, 3]
# square = lambda x: x**2
# def square(x): return x**2
# print(*map(square, numbers))
# print(*map(lambda x: x**2, numbers))


# def Fibonacci(n):
#     if n in [1, 2]:
#         return n-1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
#
#
# f_numbers = [Fibonacci(i) for i in range(1, int(input())+1)]
# print(*map(lambda x: x**3, f_numbers))

def cube(x): return x**3


def fibonacci(n):
    # return a list of fibonacci numbers
    def nth_fibo(n):
        if n in [1, 2]:
            return n-1
        else:
            return nth_fibo(n-1)+nth_fibo(n-2)

    return [nth_fibo(i) for i in range(1, n+1)]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
