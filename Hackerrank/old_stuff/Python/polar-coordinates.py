# Start Logging
import qlogger as ql
ql.start_logging(__file__)



# Run Code
try:
    import cmath
    #https://docs.python.org/3/library/cmath.html#cmath.polar
    print(*cmath.polar(complex(input())), sep='\n')

# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
