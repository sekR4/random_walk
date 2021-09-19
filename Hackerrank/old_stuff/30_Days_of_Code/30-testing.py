import random

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    lst = []
    for i in range(1,random.randint(2,30)):
        rand_int = random.randint(0,50)
        if rand_int not in lst: lst.append(rand_int) #uniques only

    @staticmethod
    def get_array():
        return TestDataUniqueValues.lst

    @staticmethod
    def get_expected_result():
        return TestDataUniqueValues.lst.index(min(TestDataUniqueValues.lst))

class TestDataExactlyTwoDifferentMinimums(object):

    lst = []
    for i in range(1,random.randint(2,30)):
        rand_int = random.randint(0,50)
        lst.append(rand_int)
    lst.append(min(lst))

    @staticmethod
    def get_array():
        # complete this function
        return TestDataExactlyTwoDifferentMinimums.lst

    @staticmethod
    def get_expected_result():
        # complete this function
        return TestDataExactlyTwoDifferentMinimums.lst.index(min(TestDataExactlyTwoDifferentMinimums.lst))

# print(TestDataUniqueValues.get_array())
# print(TestDataUniqueValues.get_expected_result())
#
# print(TestDataExactlyTwoDifferentMinimums.get_array())
# print(TestDataExactlyTwoDifferentMinimums.get_expected_result())

# class TestDataEmptyArray(object):
#
#     @staticmethod
#     def get_array():
#         # complete this function
#         return []
#
# class TestDataUniqueValues(object):
#
#     data = set()
#     while len(data) < 10:
#         data.add(random.randint(0, 100))
#
#     @staticmethod
#     def get_array():
#         # complete this function
#         data = TestDataUniqueValues.data
#         return list(data)
#
#
#     @staticmethod
#     def get_expected_result():
#         # complete this function
#         data = TestDataUniqueValues.get_array()
#         return data.index(min(data))
#
# class TestDataExactlyTwoDifferentMinimums(object):
#
#     data = set()
#     while len(data) < 9:
#         data.add(random.randint(0, 100))
#     newData = list(data)
#     newData.append(min(newData))
#
#     @staticmethod
#     def get_array():
#         # complete this function
#          data =  TestDataExactlyTwoDifferentMinimums.newData
#          return data
#
#     @staticmethod
#     def get_expected_result():
#         # complete this function
#         data = TestDataExactlyTwoDifferentMinimums.get_array()
#         return data.index(min(data))


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    print(seq)
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    print(expected_result)
    print(minimum_index(seq))
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
