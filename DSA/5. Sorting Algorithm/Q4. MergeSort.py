"""Merge Sort"""

class Solution:

    def mergeSort(self, arr):
        # Base case
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursive calls
        left = self.mergeSort(left_arr)
        right = self.mergeSort(right_arr)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        n = len(left)
        m = len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < n:
            result.append(left[i])
            i += 1

        while j < m:
            result.append(right[j])
            j += 1

        return result
