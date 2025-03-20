from typing import List
import time

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the next larger element from the right and swap
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements to the right of index i
        nums[i + 1:] = reversed(nums[i + 1:])

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1])
    ]

    for nums, expected in test_cases:
        start_time = time.time()
        solution.nextPermutation(nums)
        execution_time = (time.time() - start_time) * 1000
        print(f"Output: {nums} {'✅' if nums == expected else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")

