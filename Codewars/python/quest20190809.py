# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def duplicate_count(text):
    txt = list(set(text.lower()))
    #print(txt)

    cnt = []
    for letter in range(len(txt)):
        if text.lower().count(txt[letter]) > 1:
            cnt.append(text.lower().count(txt[letter]))
    print(len(cnt))
    return len(cnt)
    # Your code goes here

#best practice:
def duplicate_count_b(s):
    #edit for visibility
    #print(len([c for c in set(s.lower()) if s.lower().count(c)>1]))
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count_mod(s):
    #edit for visibility
    #print(len([c for c in set(s.lower()) if s.lower().count(c)>1]))
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])


text = "Indivisibilities"

duplicate_count(text)
duplicate_count_b(text)
