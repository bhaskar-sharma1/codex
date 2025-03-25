from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR all elements
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([5, 3, 5], 3),
        ([7, 7, 8, 9, 9], 8),
        ([0, 0, -1], -1),
        ([10, 20, 30, 20, 10], 30)
    ]

    for nums, expected in test_cases:
        output = solution.singleNumber(nums)
        print(f"Input: {nums} | Output: {output} {'✅' if output == expected else '❌'}")
