# I gave up here. Gues I didn't sleep enough. Still not familiar with the use of decorators

import operator


# def inner(people):
#     # complete the function
#     return map(f, sorted(people, key=lambda x: x[2]))
def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: x[2]))
    return inner


people = [
    'Mike Thomson 20 M',
    'Robert Bustle 32 M',
    'Andria Bustle 30 F']

print(person_lister(people))
# def person_lister(f):
#     def inner(people):
#         # complete the function
#         list(person.split() for person in people)
#
#     return inner
#
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
#
# if __name__ == '__main__':
#     # people = [input().split() for i in range(int(input()))]
#     people = [
#         'Mike Thomson 20 M',
#         'Robert Bustle 32 M',
#         'Andria Bustle 30 F']
#
#     print(*name_format(people), sep='\n')
