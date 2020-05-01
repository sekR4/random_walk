s = 'BANANA'

# get unique consonants/vowels to start with
consonants, vowels = [], []
for letter in set(list(s)):
    if letter not in 'AEIOU':
        consonants.append(letter)
    else:
        vowels.append(letter)

# print(consonants)

# collect points in list
stuart, kevin = [], []

stuart.append(sum([s.count(letter) for letter in consonants]))
kevin.append(sum([s.count(letter) for letter in vowels]))

print(stuart, kevin)  # first round 1 letter


def count_substring(string, sub_string):
    return sum([1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])
