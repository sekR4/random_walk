# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
# must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

# def cakes(requirements,available)
import math
# requirements = {'flour': 500, 'sugar': 200, 'eggs': 1}
# available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
#
# print(requirements)
# print(available)
#
# keys_r, vals_r = [], []
# for key, value in sorted(requirements.items()):
#     keys_r.append(key)
#     vals_r.append(value)
#
# keys_a, vals_a = [], []
# for key, value in sorted(available.items()):
#     keys_a.append(key)
#     vals_a.append(value)
#
# keys_selected = [keys_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]
# vals_selected = [vals_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]
# print(keys_r)
# print(keys_a)
# print(keys_selected)
# print(vals_selected)
#
# print(min([math.floor(i / j) for i, j in zip(vals_selected, vals_r)]))

import math

def cakes(requirements,available):
    keys_r, vals_r = [], []
    for key, value in sorted(requirements.items()):
        keys_r.append(key)
        vals_r.append(value)

    keys_a, vals_a = [], []
    for key, value in sorted(available.items()):
        keys_a.append(key)
        vals_a.append(value)

    vals_selected = [vals_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]

    if len(vals_r) != len(vals_selected):
        print(0)
        return(0)
    else:
        print(min([math.floor(i / j) for i, j in zip(vals_selected, vals_r)]))
        return min([math.floor(i / j) for i, j in zip(vals_selected, vals_r)])

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}


#best practice
def cakes(recipe, available):
    for k in recipe:
        print(available.get(k,0)/recipe[k])
    # return min(available.get(k, 0)/recipe[k] for k in recipe)

cakes(recipe,available)


name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
# keys_r,vals_r = [key,value for key, value in sorted(requirements.items())]

# print(list(requirements.keys()))
# keys_r = list(requirements.keys())
# vals_r = list(requirements.values())
#
# keys_a = list(available.keys())
# vals_a = list(available.values())

# for i in range(len(keys_a)):
#     if keys_a[i] in keys_r:
#         print(keys_a[i],i)

# vals_selected = [vals_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]
# import numpy as np
# quote = np.array(vals_selected)/np.array(vals_r)

# quote = [math.floor(i / j) for i, j in zip(vals_selected, vals_r)]
# print(min(quote))

# import math

# def cakes(requirements,available):
#     # required ingredients
#     keys_r = list(requirements.keys())
#     vals_r = list(requirements.values())
#
#     print(keys_r)
#     # print(keys_r.sort())
#
#     #available ingredients
#     keys_a = list(available.keys())
#     vals_a = list(available.values())
#
#     print(keys_a)
#
#     #relevant available ingredients
#     keys_selected = [keys_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]
#     vals_selected = [vals_a[i] for i in range(len(keys_a)) if keys_a[i] in keys_r]
#
#     print(keys_selected)
#
#     #make sure we have all
#     if len(vals_r) != len(vals_selected):
#         return 0
#         print(0)
#     else:
#         print(min([math.floor(i / j) for i, j in zip(vals_selected, vals_r)]))
#         return min([math.floor(i / j) for i, j in zip(vals_selected, vals_r)])

# cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})

# cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})

# recipe {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200} and available ingredients {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}: 8.0 should equal 11

# cakes({'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200},{'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700})
