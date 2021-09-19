# from scipy.stats import iqr
import statistics as st
n = '6'
x = '6 12 8 10 20 16'
f = '5 4 3 2 1 5'

n = int(n)
x = list(map(int, x.split()))
f = list(map(int, f.split()))

# n = int(input())
# x = list(map(int, input().split()))
# f = list(map(int, input().split()))

s = []
for number in range(len(x)):
    for i in range(f[number]):
        s.append(x[number])

# print(iqr(s,interpolation='midpoint'))

s = sorted(s)
N = sum(f)

L = s[:int(len(s)/2)]
U = s[int(len(s)/2):]

q1 = (L[int(len(L)/2)-1]+L[int(len(L)/2)])/2
q3 = (U[int(len(U)/2)-1]+U[int(len(U)/2)])/2

print(q3-q1)

# if len(s)%2 != 0:
#     q1 = st.median(s[:N//2])
#     q3 = st.median(s[N//2+1:])
# else:
#     q1 = st.median(s[:N//2])
#     q3 = st.median(s[N//2:])
#
# print(round(float(q3-q1), 1))
