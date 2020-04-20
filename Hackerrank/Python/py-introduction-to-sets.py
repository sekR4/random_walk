# Start Logging
import qlogger as ql
ql.start_logging(__file__)



# Run Code
try:
    # from collections import Counter
    # inp ='161 182 161 154 176 170 167 171 170 174'
    # heights = Counter(list(map(int,inp.split())))
    # print(heights)
    # inp = list(map(int,inp.split()))
    # print(inp)
    # print(set(inp))
    # distinct_hights = [key for key in heights]
    # print(sum(distinct_hights)/len(distinct_hights))




    def average(array):
        # distinct_hights = [key for key in Counter(array)]
        # return sum(distinct_hights)/len(distinct_hights)
        return sum(set(array))/len(set(array))

    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().split()))
        result = average(arr)
        print(result)

# Errors will be logged here
except Exception as e:
    ql.logger.exception(e)
