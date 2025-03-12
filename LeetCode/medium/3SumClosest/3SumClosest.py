from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sorting the array helps with two-pointer traversal
        closest_sum = float('inf')  # Initialize with a large value
        
        for i in range(len(nums) - 2):  # Fix one element and use two-pointer for the rest
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1  # Move left pointer to increase sum
                elif current_sum > target:
                    right -= 1  # Move right pointer to decrease sum
                else:
                    return current_sum  # Exact match, return immediately

        return closest_sum  # Return the closest sum found

# Testing function
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),  # Expected output: 2
        ([0, 0, 0], 1, 0),       # Expected output: 0
        ([1, 1, 1, 1], 3, 3),    # Expected output: 3
        ([-1, 0, 1, 1], 2, 2),   # Expected output: 2
        ([4, -1, 2, 1], 5, 5)    # Expected output: 5
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.threeSumClosest(nums, target)
        print(f"Test Case {i + 1}: nums={nums}, target={target} -> {result} {'✅' if result == expected else '❌'}")
