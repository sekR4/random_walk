
#
sample='DXXVIIII'

# if sum([1 for i in sample if i.lower() not in 'IVXLCDM'.lower()])>0:
#     print('False')
# else:
#     print('True')

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = thousand + hundred + ten + digit +'$'

import re
print(str(bool(re.match(regex_pattern, sample))))
