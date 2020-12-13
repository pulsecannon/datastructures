#!/usr/bin/env python3
"""Program to find all duplicates is a given array.

Question:

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Observations:
  1. Contents of the array are between 1 to N. i.e arr[i] is not great N or lessor than 1.
     Eg: arr =  [2, 1, 2]
         index = 1  2  3
     All elements in the array are between 0 and 2.
  2. Duplicates numbers appear exactly twice.
     Eg: arr = [2, 1, 2]
         2 appears exactly twice.
         1 appears only once.
  3. If we sort the array all duplicates are next to each other.
     Eg: arr = [2, 1, 2]
         sorted_arr = [1, 2, 2]

Solution:
  Each number in the array can be used as an index to reference the same array.
  Eg: arr =  [2, 1, 2]
      indexs  0  1  2
  Lets say element at 0th index 2 can be used to reference index 1.
  i.e for i = 0, arr[i] - 1 will be 1
      for i = 1, arr[i] - 1 will be 0
      for i = 2, arr[i] - 1 will be 1
      since 2 is duplicate it will produce the same index.
      we can multiply the value at i with -1 to tag them.

  i.e for i = 0, arr[i] - 1 will be 1 i.e arr = [2, -1, 2]
      for i = 1, arr[i] - 1 will be -2 this is a problem since index -2 is outside the array.
      so lets take absolute value of arr[i].
      for i = 1, abs(arr[i]) - 1 will be 0 ie arr = [-2, -1, 2]
      for i = 2, arr[i] - 1 will be 1 i.e arr = [-2, 1, 2]
      So 2 is a duplicate.
"""


def find_all_duplicates(numbers):
    # Output array not additional memory.
    duplicates = []
    for i in range(len(numbers)):
        # Find the reference index form the value at i.
        # absolute(arr[i]) - 1.
        index = abs(numbers[i]) - 1
        # If number at index is less than zero we have already seen this number.
        # So add it to output.
        if numbers[index] < 0:
            duplicates.append(abs(numbers[i]))
        else:
            # Else flip the value at index.
            numbers[index] = -1 * numbers[index]
    return duplicates
