# Start Logging
import qlogger as ql
ql.start_logging(__file__)



# Run Code
try:

    from itertools import permutations

    S,k = input().split()
    #my solution:
    for pm in sorted(permutations(S,int(k))):
        print(''.join(list(pm)))

    #best practice:
    # print(*[''.join(i) for i in permutations(sorted(S),int(k))],sep='\n')

    #modified:
    # print(*[''.join(list(i)) for i in sorted(permutations(S,int(k)))],sep='\n')

    # print(*[1,2,3],sep='\n') # spart den for-loop

# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
