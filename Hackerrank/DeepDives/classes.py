# Scopes and Namespaces Example
def scope_test():

    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'random test spam'

    do_local()
    # assigned spam stays within the function do_local()
    # and does NOT change the spam assigned in scope_test() (major function)
    print("After local assignment: {}\n".format(spam))

    do_nonlocal()
    # non_local spam 'leaves' its function do_nonlocal() and
    # and changes the previously defined variable in the higher hierarchy function scope_test()
    print("After nonlocal assignment: {}\n".format(spam))

    do_global()
    # the global spam did NOT become the new spam within the function scope_test()
    # insert_date it was assigned globally! (outside the main function)
    print("After global assignment: {}\n".format(spam))

# scope_test()
# print("In global scope:", spam)
# print()

# Class Objects
class MyClass:
    """A simple example class"""
    i = 'this is an attribute'

    def f(self):
        return 'this is an attribute, too'

# print(MyClass.__doc__)
# print(MyClass.i)
# print(MyClass.f(0))
# print(MyClass.f)

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(24,2)
# print(x.r, x.i)

# 9.3.3. Instance Objects

# data attributes can be assigned to a class like local variables without previous definition
x.counter = 1
while x.counter < 10:
    # print('{} * 2 = {}'.format(x.counter,x.counter * 2))
    x.counter = x.counter * 2

# print(x.counter)
del x.counter


# 9.3.4. Method Objects
# "A method is a function that “belongs to” an object." here: classes
x = MyClass()
# print('x.f():',x.f())
# print('MyClass.f(x):',MyClass.f(x))
# print('x.f() == MyClass.f(x)?','\n',x.f() == MyClass.f(x),'\n')

xf = x.f

# for i in range(3):
#     print('xf():',xf())


# 9.3.5. Class and Instance Variables
# instance variables are for data unique to each instance
# class variables are for attributes and methods shared by all instances of the class

class Dog:
    kind = 'canine'                 # class variable (shared)
    def __init__(self, name):
        self.name = name            # instance variable (unique)

example_a = Dog('Amor')
example_b = Dog('Rincewind')

# print(example_a.kind)
# print(example_b.kind,'\n')
#
# print(example_a.name)
# print(example_b.name,'\n')

class Dog:
    def __init__(self, name): # creating instance variables unique to each instance
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

example_a = Dog('Amor')
example_b = Dog('Rincewind')

example_a.add_trick('Sitz')
example_b.add_trick('Platz')

for i in [example_a,example_b]:
    print('{} kann {}.'.format(i.name,i.tricks[0]))
