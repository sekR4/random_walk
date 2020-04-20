# Start Logging
import qlogger as ql
ql.start_logging(__file__)



# Run Code
try:

    from collections import Counter

    X = int(input())
    sizes = Counter(list(map(int,input().split())))
    N = int(input())

    earning = []
    for transactions in range(N):
        request, price = map(int,input().split())
        if sizes[request] > 0:
            sizes[request] = sizes[request]-1
            earning.append(price)
    print(sum(earning))


# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
