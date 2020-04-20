# Start Logging
import qlogger as ql
ql.start_logging(__file__)

from itertools import product

# Run Code
try:
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # print(' '.join([str(tpl) for tpl in product(A,B)]))
    print(*product(A,B)) #wow!

# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
