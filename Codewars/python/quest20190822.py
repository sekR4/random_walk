# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
#
# #Example 1:
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# #Example 2: a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []

def in_array(array1, array2):
    result = []
    for word1 in range(len(array1)):
        for word2 in range(len(array2)):
            if array1[word1] in array2[word2]:
                result.append(array1[word1])
    #print(sorted(list(set(result))))
    return sorted(list(set(result)))

def in_array_best_practice(a1, a2):
    print({sub for sub in a1 if any(sub in s for s in a2)})
    print(sorted({sub for sub in a1 if any(sub in s for s in a2)}))
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})



# comparing two strings
# print("arp"=="harp")
# print(list('harp'))
# print(list("arp")==list("harp"))

# in_array(a1,a2)
in_array_best_practice(a1, a2)



# print(' '.join(list(set(a1[1].split()) & set(a2[1].split()))))
