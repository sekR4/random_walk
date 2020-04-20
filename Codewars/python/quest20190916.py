# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
# The main idea is to count all the occuring characters(UTF-8) in string.
# If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
# What if the string is empty ? Then the result should be empty object literal { }

def count(string):
    letters = sorted(list(set(string)))
    counts = [string.count(letter) for letter in letters]
    return dict(zip(letters,counts))

def count_best_practice(string):
    return {i: string.count(i) for i in string}

print(count('aba') == {'a': 2, 'b': 1})
print(count('') == {})

# s = 'aba'
# print(list(set(s)))
# s.count()

# letters = sorted(list(set(s)))
#
#
# counts = [s.count(letter) for letter in letters]
#
# dct = dict(zip(letters,counts))
# print(dct)
