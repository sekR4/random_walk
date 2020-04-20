# https://www.codewars.com/kata/scramblies/train/python
# Complete the function scramble(str1, str2) that returns true if a portion of
# str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
#     Only lower case letters will be used (a-z). No punctuation or
#     digits will be included.
#     Performance needs to be considered
# Test.assert_equals(scramble('rkqodlw', 'world'),  True)
# Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
# Test.assert_equals(scramble('katas', 'steak'), False)
# Test.assert_equals(scramble('scriptjava', 'javascript'), True)
# Test.assert_equals(scramble('scriptingjava', 'javascript'), True)

# def scramble(s1, s2):
#     letters = [letter for letter in list(s1) if letter in list(s2)]
#     # print({i: letters.count(i) for i in letters}.keys())
#     # print({i: s2.count(i) for i in s2})
#     return {i: letters.count(i) for i in letters} == {i: s2.count(i) for i in s2}


# auch falsch
# def scramble(s1, s2):
#     letters = [letter for letter in list(s1) if letter in list(s2)]
#     chks = [1 if letters.count(i) >= s2.count(i) else 0 for i in letters]
#     # return sum(chks)/len(chks) == 1 & len(chks) == len(list(set(s2)))

#auch falsch
def scramble(s1,s2):
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False
    return True

from collections import Counter

def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    return all(word[i] <= letters[i] for i in word)

# from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0


# print(scramble('rkqodlw', 'world'))
# print(scramble('rkqodlw', 'world') == True)
print(scramble('cedewaraaossoqqyt', 'codewarz'))

# s1 = 'cedewaraaossoqqyt'
# s2 = 'codewars'
#
# #for letter in set(s2)
# False if s1.count(letter) < s2.count(letter)


# print(list(s1))
# for letter in list(s1):
#     if letter in list(s2):
#         print(letter)

# # Letters match
# letters = [letter for letter in list(s1) if letter in list(s2)]
#
# # Rebuild s2 possible? check occurences
#
# print({i: s2.count(i) for i in s2})
# print({i: letters.count(i) for i in letters})
#
# for i in letters:
#     # print(i,letters.count(i),s2.count(i))
#     if letters.count(i) >= s2.count(i):
#         1
#     else:
#         0
#
# # chks = [1 for i in letters if letters.count(i) >= s2.count(i) else 0]
# chks = [1 if letters.count(i) >= s2.count(i) else 0 for i in letters]

# print(sum(chks)/len(chks)==1)
