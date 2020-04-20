if __name__ == '__main__':
    lst,scores,looser=[],[],[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        scores.append(score)

    second = min([x for x in scores if x > min(scores)])

    for i in lst:
        if i[1] == second:
            looser.append(i[0])

    for i in sorted(looser):
        print(i)
# scores = list(map(int, input().split()))
