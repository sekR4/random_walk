# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    """
    Naive approach :/. First, it's about numbers at the end of a string and
    NOT all numbers. Second, integers have a maximum by default.
    """
    wordl = list(strng)
    #find letters and digits
    letters = [letter for letter in wordl if letter in list('abcdefghijklmnopqrstuvwxyz')]
    numbers = [number for number in wordl if number not in list('abcdefghijklmnopqrstuvwxyz')]

    #merge lists
    word = ''
    for letter in range(len(letters)):
        word += letters[letter]

    number = ''
    for num in range(len(numbers)):
        number += numbers[num]

    # add 1
    if number=='':
        number=0
    number = int(number) + 1

    #handle leading zeros
    diff = len(numbers) - len(str(number))
    if diff > 0:
        number2add = diff * '0' + str(number)
    else:
        number2add = str(number)
    # print(word + number2add)
    return word + number2add

# zweiter versuch:
def increment_string_2(strng):
    """
    Naive approach :/. First, it's about numbers at the end of a string and
    NOT all numbers. Second, integers have a maximum by default.
    """
    print('string: ' + strng)
    wordl = list(strng)
    #find letters and digits
    letters = [letter for letter in wordl if letter.lower() in list('abcdefghijklmnopqrstuvwxyz')]
    numbers = [number for number in wordl if number.lower() not in list('abcdefghijklmnopqrstuvwxyz')]

    #merge lists
    word = ''
    for letter in range(len(letters)):
        word += letters[letter]
    print('word: ' + word)

    number = ''
    for num in range(len(numbers)):
        number += numbers[num]
    print('number: ' + number)

    # add 1
    if number=='':
        number=0
    # print(number)

    # number = float(number) + 1
    #
    # #handle leading zeros
    # diff = len(numbers) - len(str(number))
    # if diff > 0:
    #     number2add = diff * '0' + str(number)
    # else:
    #     number2add = str(number)
    # # print(word + number2add)
    # return word + number2add





# foo -> foo1
# foo333 -> foo334

# find digits
# print(list('foobar1'))

# for i in range(len(list('foobar1'))):
#     print(list('foobar1')[i]+1)
# print(int('f')+1)
# try:
#     int('f')
# except Exception as e:
#     raise

#find nondigits
wordl = list('foobar1')
# for i in range(len(wordl)):
#     # print(wordl[i])
#     if wordl[i] in list('abcdefghijklmnopqrstuvwxyz'):
#         # print(wordl[i])

letters = [letter for letter in wordl if letter in list('abcdefghijklmnopqrstuvwxyz')]
# print(letters)

numbers = [number for number in wordl if number not in list('abcdefghijklmnopqrstuvwxyz')]
# print(numbers)

# print(letters[0]+letters[1])
word = ''
for letter in range(len(letters)):
    word += letters[letter]

# print(word)

number = ''
for num in range(len(numbers)):
    number += numbers[num]
# print(number)


increment_string_2('WT125372294C7628KG80232325=ZLJ/3(0714239%{-8742C+I0000000610448204')




# list(set('abcdefghijklmnopqrstuvwxyz'))


# print(len(str(123)))
#
# print(int('0043'))







# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]

# def sum_pairs(ints, s):
#     for number1,number2 in range(len(ints)):
#         print(number1+number2)

# sum_pairs([10, 5, 2, 3, 7, 5], 10)

# list = [10, 5, 2, 3, 7, 5]
#
# for i,j in range(len(list)):
#     for list[j] in range(len(list)):
#         print(list[i]+list[j])
