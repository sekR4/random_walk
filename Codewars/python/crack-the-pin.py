# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python
import random
import hashlib

from itertools import permutations, combinations, chain
# assert_equals(crack("827ccb0eea8a706c4c34a16891f84e7b"), "12345")
# assert_equals(crack("86aa400b65433b608a9db30070ec60cd"), "00078")

# 5 digits in all combinations

# print(hashlib.md5('brot'.encode()).hexdigest())
# print(random.sample(range(10), 5))
# print(list(range(10)))
#
# print(hashlib.md5('12345'.encode()).hexdigest())


# crack('86aa400b65433b608a9db30070ec60cd')

n_digits = 5
n_all_combinations = 10**5
print(n_all_combinations)

combos = [''.join([str(j) for j in i])
          for i in permutations(list(range(10)), 5)]


def md5_hash(string):
    return hashlib.md5(string.encode()).hexdigest()


# for i in combos[:100]:
#     print(i)


permuts = dict(zip(map(md5_hash, combos), combos))
# for key in permuts.keys():
#     print(key)

# print(permuts['86aa400b65433b608a9db30070ec60cd'])

combos = list(permutations(list(range(10)), 5))
combos2 = list(combinations(list(range(10)), 5))
# print(len(combos), len(combos2))

print(min(combos))
print(min(combos2))

# for c in range(len(combos[:10])):
#     print(combos[c], combos2[c])


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))


# for subset in all_subsets(list(range(10))):
#     print(subset)

def combiner():
    digits, d_list = '0123456789', []
    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    for e in digits:
                        d_list.append(a+b+c+d+e)
    return d_list


def crack(hash_str):
    digits, d_list = '0123456789', []
    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    for e in digits:
                        d_list.append(a+b+c+d+e)

    def md5_hash(string):
        return hashlib.md5(string.encode()).hexdigest()
    all_combinations = dict(zip(map(md5_hash, d_list), d_list))
    return all_combinations[hash_str]


print(crack("827ccb0eea8a706c4c34a16891f84e7b"))

# best practice & clever solution


def crack(hash_str, n_digits):
    for i in range(10**n_digits):
        if hashlib.md5(str(i).zfill(n_digits).encode()).hexdigest() == hash_str:
            return str(i).zfill(n_digits)


print(crack("827ccb0eea8a706c4c34a16891f84e7b", 5))
