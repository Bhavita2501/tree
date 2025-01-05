"""
   1. Select the last element as the _pivot value_.
   1. Move the left bound to the right until it reaches a value greater than or equal to the pivot.
      - Using `left_ix`, sweep the array from left to right while it is < _pivot value_
   1. Move the right bound to the left until it crosses the left bound or finds a value less than the pivot.
      - Using `right_ix`, sweep the array from the right to the left while it is >= _pivot value_
   1. Check if partitioning is complete
"""
from icecream import ic
def partitionArray(arr, left_ix, right_ix):
    pivot_index = right_ix
    pivot =  arr[pivot_index]
    while left_ix <= right_ix:
        while arr[left_ix] < pivot:
            left_ix += 1
        while left_ix <= right_ix and arr[right_ix] >=  pivot:
            right_ix -= 1
        if left_ix >= right_ix:
            # swap values referenced by `left_ix` and `pivot_ix`
            # partitioning complete
            arr[left_ix], arr[pivot_index] = arr[pivot_index], arr[left_ix]
        else:
            # swap values referenced by `left_ix` and `right_ix`
            arr[left_ix], arr[right_ix] = arr[right_ix], arr[left_ix]
    return left_ix
def quick_sort(array, left_bound, right_bound):
    ic(array, left_bound, right_bound)
    if right_bound- left_bound <= 1:
        return array
    else:
        pivot = partitionArray(array, left_bound, right_bound)
        quick_sort(array, left_bound, pivot-1)
        quick_sort(array, pivot+1, right_bound)
    return array
"""[1, 2, 4, 0, 5, 3]
    0  1  2  3  4  5

quick_sort(array, left_bound, right_bound)
quick_sort(0, 5), pivot_ix = 3
   left: quick_sort(0, 2), pivot: 2
      left: quick_sort(0,1), pivot: 1
         left: quick_sort(0,0)  -- [a]
         right: quick_sort(2,1) -- []
      right: quick_sort(3,2) -- []
   right: quick_sort(4, 5), pivot: 5
      left: quick_sort(4,4) -- [a]
      right: quick_sort(6,5) -- []
ic(quick_sort([1, 2, 4, 0, 5, 3], 0, 5))
"""
ic(quick_sort([1, 2, 4, 0, 5, 3], 0, 5))

# import unittest
# class TestFunction(unittest.TestCase):
#     def test_1_digit(self):
#         self.assertEqual(partitionArray([1, 2, 4, 0, 5, 3], 0, 5), [1, 2, 0, 3, 5, 4])
# unittest.main()
