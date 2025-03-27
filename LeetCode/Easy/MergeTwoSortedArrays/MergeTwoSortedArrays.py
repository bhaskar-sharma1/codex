from typing import List
import unittest

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1  # Pointers for nums1, nums2, and final position
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If elements are left in nums2, copy them (nums1 elements are already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class TestMergeSortedArray(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_case_2(self):
        nums1 = [1]
        nums2 = []
        Solution().merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_case_3(self):
        nums1 = [0]
        nums2 = [1]
        Solution().merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

    def test_case_4(self):
        nums1 = [4,5,6,0,0,0]
        nums2 = [1,2,3]
        Solution().merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()
