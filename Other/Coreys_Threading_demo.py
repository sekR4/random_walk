#https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Threading/threading-demo.py
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


# Test with threading
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

# Test without threading
secs = [5, 4, 3, 2, 1]
print(*map(do_something,secs),sep='\n')

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
