import re

for i in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
#     sample = input()
#     if all([len(re.findall('\.\d+', sample)) > 0,
#             len(re.findall('\+|\-', sample)) < 2,
#             len(re.findall('[a-zA-Z]', sample)) == 0]):
#         print(isinstance(eval(sample), float))
#     else:
#         print('False')


cases = ['1.414', '+.5486468', '0.5.0', '1+1.0', '0']
results = ['True', 'True', 'False', 'False', 'False']


for i in range(len(cases)):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', cases[i])))

# for i in range(len(cases)):
#     sample = cases[i]
#     print(len(sample.split('.')))
# if all([len(re.findall('\.\d+', sample)) > 0,
#         len(re.findall('\+|\-', sample)) < 2,
#         len(re.findall('[a-zA-Z]', sample)) == 0]):
#     print(isinstance(eval(sample), float))
# else:
#     print('False')

# T = ['+4.50', '-1.0', '.5', '-.7', '+.4', '12.0']
#
# F = ['-+4.5', '12.', '4.0O0']
#
# for sample in F:
# after_dot = re.findall('\.\d+', sample)
# condition 1: len(after_dot) > 0
# before_dot = re.findall('\+|\-', sample)
# condition 2: len(before_dot) < 2
# print(sample)
# print(re.findall('[a-zA-Z]', sample))

# print(sample)
# print(len(re.findall('\.\d+', sample)) > 0)
# print(len(re.findall('\+|\-', sample)) < 2)
# if len(re.findall('\.\d+', sample)) > 0 & len(re.findall('\+|\-', sample)) < 2:
#     print(sample)
# print(isinstance(eval(sample), float))
# print(all([len(re.findall('\.\d+', sample)) > 0,
#            len(re.findall('\+|\-', sample)) < 2,
#            isinstance(eval(sample), float)]))
