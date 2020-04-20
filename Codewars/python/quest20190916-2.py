# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    return list(set([i for i in seq if (seq.count(i) % 2) != 0]))[0]

def find_it_best_practice(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5)

string =[20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]


print({i: string.count(i) for i in string if (string.count(i) % 2) != 0})


print(list({i: string.count(i) for i in string if (string.count(i) % 2) != 0}.keys())[0])
print({i: string.count(i) for i in string if (string.count(i) % 2) != 0}.items())

# for i in string:
#     if (string.count(i) % 2) != 0:
#         print(i)
odd = list(set([i for i in string if (string.count(i) % 2) != 0]))[0]
print(odd)
