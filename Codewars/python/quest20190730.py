strings = ["4556364607935616","64607935616","1","","Skippy","Nananananananananananananananana Batman!"]
# for string in strings:
#     print(string)

#print('length strings: {}'.format(len(strings)))

def maskify(something):
    something = str(something)
    str_len = len(something)
    if str_len <= 4:
        result = something
    elif str_len > 4:
        to_show = something[-4:]
        len_dont_show = str_len - 4
        result = str(len_dont_show * '#') + to_show
    return result

for string in strings:
    print(maskify(string))

#print(maskify(1))
