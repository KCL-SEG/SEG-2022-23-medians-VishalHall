"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from math import ceil, floor


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
if numbers:
    numbers.sort()
    numbers_length = len(numbers)
    if numbers_length % 2 == 1:
        print(numbers[numbers_length // 2])
    else:
        print((numbers[numbers_length // 2] + numbers[numbers_length // 2 - 1]) / 2)