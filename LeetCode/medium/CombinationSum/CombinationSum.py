from typing import List
import time

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
        
        candidates.sort()  # Sorting helps optimize by stopping early for larger numbers
        backtrack(0, target, [])
        return result

# Test Cases
if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, [])
    ]

    for candidates, target, expected in test_cases:
        start_time = time.time()
        result = solution.combinationSum(candidates, target)
        execution_time = (time.time()-start_time)*1000
        print(f"Test Case: candidates = {candidates}, target = {target}")
        print(f"Output: {result} {'✅' if sorted(result) == sorted(expected) else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")
