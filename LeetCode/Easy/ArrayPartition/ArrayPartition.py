import unittest
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Given an integer array nums of 2n integers, group these into pairs 
        such that the sum of min(ai, bi) for all pairs is maximized.
        """
        ############### Approach 1. ################
        '''
        nums.sort()  # Sorting in ascending order
        return sum(nums[i] for i in range(0, len(nums), 2))
        '''
        ################ Approach 2. ###############
        # The possible range is from -10,000 to 10,000.
        # Using underscores for readability.
        min_val, max_val = -10_000, 10_000
        count = [0] * (max_val - min_val + 1)  # Frequency array for range [-10000, 10000]

        # Step 1: Fill frequency array
        for num in nums:
            count[num - min_val] += 1

        # Step 2: Process pairs using counting sort logic
        pair_sum = 0
        take = True  # Determines whether to take the element into the sum
        for i in range(len(count)):  
            while count[i] > 0:
                if take:
                    pair_sum += i + min_val  # Convert index back to original number
                take = not take  # Flip take for alternating pairs
                count[i] -= 1

        return pair_sum

# Unit tests
class TestArrayPairSum(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([1, 2, 2, 5, 6, 6], 9),
            ([1, 2], 1),
            ([-2, -1, 0, 5], -2),  # Fixed expected value
            ([0, 0, 1, 1], 1),
            ([-10000, -9999, 9999, 10000], -1),  # Fixed expected value
            ([1, 1, 1, 1], 2),
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                result = solution.arrayPairSum(nums)
                
                # Printing input, output, and status
                print(f"Input: {nums} | Output: {result} {'✅' if result == expected else '❌'}")
                
                # Assertion for unittest
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
