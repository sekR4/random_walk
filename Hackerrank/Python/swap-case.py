def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i]=s[i].upper()
        else: s[i]=s[i].lower()
    result = ''
    for _ in s:
        result = result+_
    return result

if __name__ == '__main__':
    print(swap_case(input()))


# s = 'HackerRank.com presents "Pythonist 2".'
# # for letter in s:
# #     if letter.islower():
# #         print(letter)
#
# s = list(s)
# for i in range(len(s)):
#     if s[i].islower():
#         s[i]=s[i].upper()
#     else: s[i]=s[i].lower()
#
# result = ''
# for _ in s:
#     result=result+_
# print(result)
