# import re
#
# n = int(input())

# def regexp_substr(string,pattern):
#     """ Takes 2 strings as input.
#         Returns None when pattern not found. """
#     p=re.compile(pattern)
#     try: out = p.findall(string)[0]
#     except: out = None
#     return out
#
# n_bin = regexp_substr(bin(n),'\d+$')

current_occ = 0
longest_occ = 0

for number in bin(int(input())):
    if number == '1': current_occ += 1
    else: longest_occ, current_occ = max(current_occ, longest_occ), 0

print(max(current_occ, longest_occ))
