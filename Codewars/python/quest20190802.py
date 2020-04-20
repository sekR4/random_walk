#Find the missing letter
# Example:
#
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):

    alphabet = list(set('abcdefghijklmnopqrstuvwxyz'))
    alphabet.sort()
    # for letter in alphabet:
    #     print(letter)
    for i in range(len(alphabet)):
        print(i,alphabet[i])
    # print(alphabet)
    return

# alphabet = list(set('abcdefghijklmnopqrstuvwxyz'))
# alphabet.sort()
# print(alphabet)

letters = ['a','b','c','d','f']
find_missing_letter(letters)
