from typing import List

class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left  # The correct insert position

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 3, 5, 6], 5, 2),  # Expected output: 2
        ([1, 3, 5, 6], 2, 1),  # Expected output: 1
        ([1, 3, 5, 6], 7, 4),  # Expected output: 4
        ([1, 3, 5, 6], 0, 0),  # Expected output: 0
        ([1], 0, 0),  # Expected output: 0
        ([1], 2, 1)   # Expected output: 1
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.search_insert(nums, target)
        print(f"Test Case {i + 1}: nums={nums}, target={target} -> {result} {'✅' if result == expected else '❌'}")
