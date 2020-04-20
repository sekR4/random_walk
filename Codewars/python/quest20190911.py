# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    pieces = text.split()
    sentence=''
    for piece in pieces:
        if piece not in list('.,:!?'):
            # print(piece[1:]+piece[0]+'ay')
            sentence += ' '+ piece[1:]+piece[0]+'ay'
        else:
            # print(piece)
            sentence += ' ' + piece
    print(sentence)
    return sentence.lstrip()

print(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
# pig_it('This is my string')

print(len(pig_it('Pig latin is cool')), len('igPay atinlay siay oolcay'))

# best practice solution:
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# text = 'Haha !'
# print(text.split())
# pieces = text.split()
#
# sentence=''
# for piece in pieces:
#     if piece not in list('.,:!?'):
#         # print(piece[1:]+piece[0]+'ay')
#         sentence += ' '+ piece[1:]+piece[0]+'ay'
#     else:
#         # print(piece)
#         sentence += ' ' + piece

# print(sentence)
# wort='hallo'
# print(wort[1:]+wort[0]+'ay')


# idx_piece = list(range(len(pieces)))
# idx_punct = [1 if piece in list('.,:!?') else 0 for piece in pieces]
# dct = dict(zip(pieces,zip(idx_piece,idx_punct)))
# print(dct)
# print(dct.get(pieces[0]))
# print(pieces[0],'idx_piece:',list(dct[pieces[0]])[0],'idx_punct:',list(dct[pieces[0]])[1])

# for piece in range(len(pieces)):
#     print(pieces[piece],'idx_piece:',list(dct[pieces[piece]])[0],'idx_punct:',list(dct[pieces[piece]])[1])
# print(idx_punct)


# for piece in pieces:
#     if piece in list('.,:!?'):
#         print(1)
#     else:
#         print(0)
#
# print(dict(zip(pieces,zip(idx_piece,idx_punct))))

# print(list(range(6)))
