# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
# test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
# test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
# test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)


 # Three 6's =>  600 points
 # Three 5's =>  500 points
 # Three 4's =>  400 points
 # Three 3's =>  300 points
 # Three 2's =>  200 points
 # Three 1's => 1000 points

 # One   1   =>  100 points
 # One   5   =>   50 point

throw = [5,5,5,5,1]

for i in [6,5,4,3,2,1]:
    # print(i, throw.count(i))
    if i>1 and throw.count(i) >= 3:
        print(i*100, '\n')

    if i == 1 and throw.count(i) >= 3:
        print(1000)

    if i == 1 and throw.count(i) >= 4:
        print((throw.count(i)-3)*100)

    if i == 1 and throw.count(i) < 3:
        print(throw.count(i)*100)

    if i == 5 and throw.count(i) < 3:
        print(throw.count(i)*50)

    if i == 5 and throw.count(i) >= 4:
        print((throw.count(i)-3)*50)


for i in [6,5,4,3,2,1]:
    # print(i, throw.count(i))
    if i>1 and throw.count(i) >= 3:
        print(i*100)

    if i == 1:
        if throw.count(i) >= 3:
            print(1000)
        if throw.count(i) >= 4:
            print((throw.count(i)-3)*100)
        if throw.count(i) < 3:
            print(throw.count(i)*100)

    if i == 5:
        if throw.count(i) < 3:
            print(throw.count(i)*50)
        if throw.count(i) >= 4:
            print((throw.count(i)-3)*50)



    # if i == 1 and throw.count(i) >= 3:
    #     print(1000)
    #
    # if i == 1 and throw.count(i) >= 4:
    #     print((throw.count(i)-3)*100)
    #
    # if i == 1 and throw.count(i) < 3:
    #     print(throw.count(i)*100)
    #
    # if i == 5 and throw.count(i) < 3:
    #     print(throw.count(i)*50)
    #
    # if i == 5 and throw.count(i) >= 4:
    #     print((throw.count(i)-3)*50)

def score(throw):
    score = []
    for i in [6,5,4,3,2,1]:
        if i>1 and throw.count(i) >= 3:
            score.append(i*100)

        if i == 1:
            if throw.count(i) >= 3:
                score.append(1000)
            if throw.count(i) >= 4:
                score.append((throw.count(i)-3)*100)
            if throw.count(i) < 3:
                score.append(throw.count(i)*100)

        if i == 5:
            if throw.count(i) < 3:
                score.append(throw.count(i)*50)
            if throw.count(i) >= 4:
                score.append((throw.count(i)-3)*50)

    return sum(score)


throw = [1,2,3,3,3]

score(throw)

#best practice
def score(dice):
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice:
    counter[die-1] += 1

  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum
