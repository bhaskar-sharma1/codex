from typing import List
import time

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
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

# 🔹 Function to calculate time complexity analysis
def calculate_time_complexity(n: int):
    return f"O(n³) -> Worst case for fourSum with nested loops."

# 🔹 Testing function with execution time measurement
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),  
        ([2,2,2,2,2], 8, [[2,2,2,2]]),  
        ([1,1,1,1,1], 4, [[1,1,1,1]]),  
        ([-3,-1,0,2,4,5], 3, [[-3,-1,2,5], [-3,0,2,4]]),  
        ([0,0,0,0,0,0], 0, [[0,0,0,0]])  
    ]

    print(f"Time Complexity: {calculate_time_complexity(len(test_cases[0][0]))}\n")

    for i, (nums, target, expected) in enumerate(test_cases):
        start_time = time.time()  # Start measuring time
        result = sol.fourSum(nums, target)
        execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        result.sort()  # Sort the output for proper comparison
        expected.sort()  # Sort expected output as well
        
        print(f"Test Case {i + 1}: nums={nums}, target={target} -> {result} {'✅' if result == expected else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")