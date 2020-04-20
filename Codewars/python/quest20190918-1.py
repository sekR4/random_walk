# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123]#, 2333, 144, 50, 132, 123, 34, 89]
xs = [30,20,10,1]
# Test.assert_equals(choose_best_sum(230, 4, xs), 230)
# Test.assert_equals(choose_best_sum(430, 5, xs), 430)
# Test.assert_equals(choose_best_sum(430, 8, xs), None)

# max(k distances) <= maxMiles


def choose_best_sum(maxMiles, numCities, distances):
    """
    maxMiles:   integer - Maximum of miles John wants to drive
    numCities:  integer - Number of cities John and Mary want to visit
    distances:  list - distances between cities
    """
    # 1. numCities elements of [distances] must be summed
    # 2. for all possible combinations
    print('distances: ', distances)
    print('numCities: ', numCities)
    for distance in distances:
        for city in range(numCities):
            print(distance + distances[city],'=', distance,'+',distances[city])
        # print('distance: ',distance)
        # print('distances[0]+distance: ', distances[0]+distance)

print(choose_best_sum(230, 2, xs))
