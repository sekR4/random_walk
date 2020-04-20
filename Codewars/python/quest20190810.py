# Quest 2:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    print((len(str(num))-1)*'0')
    pass

expanded_form(70304)

# Quest 1
# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible,
# containing distinct letters, each taken only once -
# coming from s1 or s2.

# a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
def longest(s1, s2):
    txt = list(''.join(set(s1 + s2)))
    txt.sort()
    print(''.join(txt))
    return ''.join(txt)

# best practice
def longest(a1, a2):
    #print("".join(sorted(set(a1 + a2))))
    return "".join(sorted(set(a1 + a2)))

longest(a, b)
