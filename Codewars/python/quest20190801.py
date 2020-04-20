x = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

def openOrSenior(data):
    # if age >= 55 & handycap >7  -> Senior
    #print('#newMembers {}'.format(len(data)))
    results = []
    for member in range(len(data)):
        #print(data[member][0],data[member][1])
        if (data[member][0] >= 55) & (data[member][1] > 7):
            results.append('Senior')
        else:
            results.append('Open')
    # print(results)
    return results

openOrSenior(x)

#best practice:
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
