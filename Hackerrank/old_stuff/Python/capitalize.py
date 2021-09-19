# Start Logging
import qlogger as ql
ql.start_logging(__file__)
import os


# Run Code
try:
    # sample_input = 'chris alan'

    def solve(s):
        a,b = s.split()
        res = tuple(a.capitalize(), b.capitalize())
        return res

        # for x in s[:].split():
        #     s = s.replace(x, x.capitalize())
        # print(s)

    # solve(sample_input)
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        s = input()

        result = solve(s)

        fptr.write(result + '\n')

        fptr.close()

# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
