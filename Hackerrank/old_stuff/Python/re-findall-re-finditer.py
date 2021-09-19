import re

# sample, results = 'abaabaabaabaae', []
# tribute goes to giacgbj
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
# alternative: [%s]([%s]{2,})(?=[%s])
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags=re.I)
print('\n'.join(m or ['-1']))
# for i in re.finditer('([aeiouAEIOU]+)', sample):
#     vowel_seq = i.span()[1] - i.span()[0]
#     if (vowel_seq >= 2) and \
#         (sample[i.span()[1]-vowel_seq-1].lower() in 'qwrtypsdfghjklzxcvbnm') and \
#             (sample[i.span()[1]].lower() in 'qwrtypsdfghjklzxcvbnm'):
#         # print(i[0])
#         results.append(i[0])
#
# if len(results) > 0:
#     print(*results, sep='\n')
# else:
#     print(-1)

# sample = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
# finding vowels via regex
# print(re.findall('([aeiouAEIOU]+)', sample))
# print(*re.finditer('([aeiouAEIOU]+)', sample), sep='\n')
