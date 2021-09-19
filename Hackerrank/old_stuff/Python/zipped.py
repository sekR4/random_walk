_, subjects = map(int, input().split())

scores = []
for subject in range(subjects):
    scores.append(list(map(float, input().split())))

[print(sum(student)/len(student)) for student in zip(*scores)]
