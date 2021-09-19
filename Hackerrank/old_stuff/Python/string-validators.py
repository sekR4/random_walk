# if __name__ == '__main__':
#     s = input()
#     if sum([letter.isalnum() for letter in s]) > 0: print('True')
#     else: print('False')
#
#     if sum([letter.isalpha() for letter in s]) > 0: print('True')
#     else: print('False')
#
#     if sum([letter.isdigit() for letter in s]) > 0: print('True')
#     else: print('False')
#
#     if sum([letter.islower() for letter in s]) > 0: print('True')
#     else: print('False')
#
#     if sum([letter.isupper() for letter in s]) > 0: print('True')
#     else: print('False')

    # print(s.isalnum())
    # print(s.isalpha())
    # print(s.isdigit())
    # print(s.islower())
    # print(s.isupper())

# best practice:
if __name__ == '__main__':
    s = input()
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
