import time
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sorting is O(n log n)
        res = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # Pruning
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:  # Pruning
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:  # Pruning
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:  # Pruning
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

# Function to measure execution time
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    return result, execution_time

# Testing function
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([1, 1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
        ([-3, -1, 0, 2, 4, 5], 3, [[-3, -1, 2, 5], [-3, 0, 2, 4]]),
        ([0, 0, 0, 0, 0, 0], 0, [[0, 0, 0, 0]])
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result, execution_time = measure_execution_time(sol.fourSum, nums, target)

        result.sort()  # Sorting for consistent comparison
        expected.sort()

        print(f"Test Case {i + 1}: nums={nums}, target={target} -> {result} {'✅' if result == expected else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")
