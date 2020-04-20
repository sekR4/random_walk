# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# Test.expect(xo('xo'), 'True expected')
# Test.expect(xo('xo0'), 'True expected')
# Test.expect(not xo('xxxoo'), 'False expected')



# funktioniert noch nicht bei 3 unterschiedlichen buchstaben
# def xo(s):
#     #check for x and o
#     if 'x' in s:
#         x = 1
#     else:
#         x = 0
#     if 'o' in s:
#         o = 1
#     else:
#         o = 0
#     #print(x,o)
#
#     #count distinct letters
#     letters = list(set(s.lower()))
#     #print(letters)
#
#     cnt = []
#     for letter in range(len(letters)):
#         cnt.append(s.lower().count(letters[letter]))
#
#     if len(cnt) >= 2:
#         diff = cnt[0]-cnt[1]
#
#         if diff == 0:
#             if (x+o == 2) or (x+o == 0):
#                 print('True')
#                 return True
#         else:
#             print('False')
#             return False
#     print('True')
#     return True

def xo(s):
    s = s.lower()
    return print(s.count('x') == s.count('o'))
# xo('ooxxx')
# s = 'ooxx'
# letters = list(set(s))
# print(letters)
#
# for letter in range(len(letters)):
#     print(s.count(letters[letter]))
xo(xxxxJxxxxxxdQooovtxENxxxkxxomUooxooxx) #should be False
