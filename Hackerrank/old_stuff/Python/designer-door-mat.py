# Start Logging
import qlogger as ql
ql.start_logging(__file__)


# Run Code
try:

    N,M = map(int, input().split())
    pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]
    print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))


# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
