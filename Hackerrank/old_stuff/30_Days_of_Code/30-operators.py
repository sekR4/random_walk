mealCost=float(input())
tipPercent=int(input())
taxPercent=int(input())

tip = mealCost*(tipPercent/100)
tax = mealCost*(taxPercent/100)
total = mealCost + tip + tax

print(round(total))

# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the solve function below.
# def solve(meal_cost, tip_percent, tax_percent):
#
# if __name__ == '__main__':
#     meal_cost = float(input())
#
#     tip_percent = int(input())
#
#     tax_percent = int(input())
#
#     solve(meal_cost, tip_percent, tax_percent)
