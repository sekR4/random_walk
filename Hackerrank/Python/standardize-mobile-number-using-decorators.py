# https://wiki.python.org/moin/Generators
def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 "+c[-10:-5]+" "+c[-5:] for c in l)  # thx to RankBank
    return fun


@wrapper
def sort_phone(l):
    print(type(l))
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    # submission
    # l = [input() for _ in range(int(input()))]
    # testing
    l = [
        '07895462130',
        '919875641230',
        '9195969878']
    sort_phone(l)
