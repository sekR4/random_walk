import re
from itertools import groupby

def len_iter(items):
    return sum(1 for _ in items)

def consecutive_one(data):
    return max(len_iter(run) for val, run in groupby(data) if val)

card_numbers = {}

n = int(input())
for _ in range(n):

    number = input()

    # number fractions
    _ = ''
    for j in number.split('-'):
        if len(re.sub('[^0-9]','', j))==4:
            _ +=j

    # valid conditions
    if number[0] in ['4','5','6'] \
    and (len(_) == 16 or (len(number)==16 \
    and len(re.sub('[^0-9]','', number)) == 16)) \
    and consecutive_one(re.sub('[^0-9]','',number)) < 4 \
    and (len(re.sub('\w','',number))==0 or len(re.sub('\w','',number))==3):
        card_numbers['{}'.format(number)] = 'Valid'
    else:
        card_numbers['{}'.format(number)] = 'Invalid'

for i in card_numbers:
    print(card_numbers[i])
    # print(i.split('-'))
    # _ = ''
    # for j in i.split('-'):
    #     if len(j)==4:
    #         _ +=j
    # if len(_)==16:
    #     print('yeah')
    # else:
    #     print('no')
    # print(regexp_substr(i,'[0-9]+'))
    # print(re.match(r'^([\s\d]+)$', i))
    # print(regexp_substr(i,'\d*'))
    # print(re.sub('[^0-9]','', i))





# print(consecutive_one(re.sub('[^0-9]','','5133-3367-8912-3456')))

    # 4
    #
    # 3695-7963-  5827-75
    #
    # 4143-4672-8798-2968-2968
    #
    # 6865---------------3965---------------1564-------------2918
    #
    # 6865396515642918

#     Expected Output
# Download
#
#     Invalid
#
#     Invalid
#
#     Invalid
#
#     Valid

print(re.sub('\w','', '6865---------------3965---------------1564-------------2918'))
