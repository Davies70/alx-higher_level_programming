#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity \
        (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm:\
        O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """ find the peak of an integer """
    nums = list_of_integers
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = int(left + (right - left) / 2)
        if (nums[mid] < nums[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return nums[left]
