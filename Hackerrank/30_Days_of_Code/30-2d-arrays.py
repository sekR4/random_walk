str1 = '1 1 1 0 0 0'
str2 = '0 1 0 0 0 0'
str3 = '1 1 1 0 0 0'
str4 = '0 0 2 4 4 0'
str5 = '0 0 0 2 0 0'
str6 = '0 0 1 2 4 0'

strgs=[str1,str2,str3,str4,str5,str6]

matrix = []
for strg in strgs:
    matrix.append(list(map(int, strg.split())))

# print(matrix)
for row in matrix:
    print(row)



sums = []
for x in range(0,4):
    for y in range(0,4):
        # print(matrix[x][y:y+3])
        # print(matrix[x+1][y+1])
        # print(matrix[x+2][y:y+3])
        # print()

        sum1 = sum(matrix[x][y:y+3])
        sum2 = matrix[x+1][y+1]
        sum3 = sum(matrix[x+2][y:y+3])

        sums.append(sum1+sum2+sum3)
        print(sum1+sum2+sum3)

print(sums)
print(max(sums))


#submission:

matrix,sums = [],[]
for i in range(6):
    matrix.append(list(map(int, input().rstrip().split())))

for x in range(0,4):
    for y in range(0,4):
        sum1 = sum(matrix[x][y:y+3])
        sum2 = matrix[x+1][y+1]
        sum3 = sum(matrix[x+2][y:y+3])
        sums.append(sum1+sum2+sum3)

print(max(sums))
