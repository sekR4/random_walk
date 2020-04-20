# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
# Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
# Test.assert_equals(sort_array([]),[])

# some_numbers = [5, 3, 2, 8, 1, 4]
# print(some_numbers)
# #idx? v1 works
# odds=[]
# idxs=[]
# for i in range(len(some_numbers)):
#     if (some_numbers[i] % 2) != 0:
#         odds.append(some_numbers[i])
#         idxs.append(i)
#
# print('odds: {}'.format(odds))
# print('idxs: {}'.format(idxs))
#
# odds = sorted(odds)
#
# for i,j in zip(idxs,odds):
#     # print(i,j)
#     some_numbers[i] = j
#
# print(some_numbers)


def sort_array(numbers):
    print(numbers)
    odds,idxs = [],[]
    for i in range(len(numbers)):
        if (numbers[i] % 2) != 0:
            odds.append(numbers[i])
            idxs.append(i)
    print(odds)
    print(idxs)
    for i,j in zip(idxs,sorted(odds)):
        numbers[i] = j
    print(numbers)


def sort_array(numbers):
    odds,idxs = [],[]

    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odds.append(numbers[i])
            idxs.append(i)

    for i,j in zip(idxs,sorted(odds)):
        numbers[i] = j
    return numbers

sort_array([5, 3, 1, 8,0])

#best practice
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  # odds = sorted((x for x in arr if x%2 != 0)) #mod
  print([x if x%2==0 else odds.pop() for x in arr]) #mod
  # return [x if x%2==0 else odds.pop() for x in arr]

# Er kann mit pop() über die Liste iterieren, ohne sie extra mit neuem
# index mit zu benennen. Das macht den Loop unkomplizierter. Genial!


sort_array([5, 3, 1, 8,0])

list2 = [1, 2, 3, ('cat', 'bat'), 4]

# pop() is an inbuilt function in Python that removes and returns last value
# from the list or the given index value.

# Pop last three element
print(list2.pop())
print(list2.pop())
print(list2.pop())


# numbers = [1,2,3]
# for i in numbers:
#     print(numbers.pop(),i)







# out=[]
# for i in range(len(some_numbers)):
#     for j,odd in enumerate(odds):
#         if


# Python code to replace every element
# in second list with index of first element.

# List initialization
# Input1 = ['cut', 'god', 'pass']
#
# # using enumeate
# temp = {y:x for x, y in enumerate(Input1)}
#
# # List initialization
# Input2 = ['god', 'cut', 'cut', 'cut',
# 		'god', 'pass', 'cut', 'pass']
#
# # Using list comprehension
# Output = [temp.get(elem) for elem in Input2]
#
# # Printing output
# print("initial 2 list are")
# print(Input1, "\n", Input2)
# print("Second list after replacement is:", Output)
#
# print(temp)



# [odd for odd in odds if (number % 2) != 0 else number for number in some_numbers]

# https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list
# for idx, number in enumerate(some_numbers):
#     # print(idx, number)
#     if (number % 2) != 0:
#         for odd in sorted(odds):
#             some_numbers[idx] = odd


# odds = sorted(odds)
# for idx, i in enumerate(idxs):
#     print(some_numbers[idx],i)

# for odd in range(len(sorted(odds))):
#     for idx, number in enumerate(some_numbers):
#         # print(idx, number)
#         if (number % 2) != 0:
#                 some_numbers[idx] = sorted(odds)[odd]
#
# print(some_numbers)
