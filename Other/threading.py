# https://www.youtube.com/watch?v=IEEhzQoKtQU
# Theoretically threading should not give a performanc boost here,
# since it is a CPU operation. Right?
# Interestingly, already importing concurrent.futures crashes the script

import concurrent.futures
# from concurrent.futures.thread import ThreadPoolExecutor
import time

start = time.perf_counter()

numbers = list(range(100000))


def Its_hip_to_be_square(number):
    return number**2


# print(*map(Its_hip_to_be_square, numbers), sep='\n')
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(Its_hip_to_be_square, numbers)
    for result in results:
        print(result)

print(f'Finished in {round(time.perf_counter()-start, 2)} second(s)')
