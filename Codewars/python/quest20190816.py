# Make a program that filters a list of strings and returns a list with
# only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has
# to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
# i.e.
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

names = ["Ryan", "Kieran", "Mark"]
def friend(x):
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    print(friends)
    return friends
    #Code

friend(names)

def friend2(x):
    print([name if len(name) == 4 else None for name in x])
    # return
friend2(names)

def friend_best_practice(x):
    print([f for f in x if len(f) == 4])
    return [f for f in x if len(f) == 4]

friend_best_practice(names)
