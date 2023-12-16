import unittest


def selection_sort(array):
    for i in range(0, len(array)):
        min_value = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n ^ 2).
* Auxiliary space: O(1).
* Total space: O(n).
"""


def selection_sort_solution(arr):
    # iterate through the array from left to right
    for i in range(len(arr)):
        # set the ith index to be the intial min variable
        min = i
        # Iterate from the ith index to n - 1 to find the ith smallest element and swap it with arr[i]
        for inner in range(i, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
        (arr[i], arr[min]) = (arr[min], arr[i])

    return arr


class TestYourSortingAlgorithm(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_sorted_list(self):
        sorted_list = selection_sort([1, 2, 3, 4, 5])
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        reversed_list = selection_sort([5, 4, 3, 2, 1])
        self.assertEqual(reversed_list, [1, 2, 3, 4, 5])

    def test_random_list(self):
        unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_list = selection_sort(unsorted_list)
        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_duplicates(self):
        list_with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_list = selection_sort(list_with_duplicates)
        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
