# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.

# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                print('False')
                return False

                break
        # else:
        #     if num == 4:
        #         print('False')
        #         return False
        #     else:
        #         print('True')
        #         return True
        else:
            return True

    else:
        # print('False')
        return False

def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
                break
        else:
            if num == 4:
                return False
            else:
                return True
    else:
        return False


# for s in range(5):
#     if is_prime(s) == 'True':
#         print(s)

is_prime(13)
