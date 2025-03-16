import time
from typing import List

PHONE_MAP = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs","8": "tuv", "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                res.append(path)
                return
            for char in PHONE_MAP[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res

# Testing with execution time measurement
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        # (digits, expected_output)
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
        ("79", ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]),
        # Updated the expected output for "234" with the correct 27 combinations
        ("234", [
            "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
            "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
            "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
        ])
    ]

    print("\n🔹 Running Test Cases with Execution Time:\n")

    for i, (digits, expected) in enumerate(test_cases):
        start_time = time.time()
        result = sol.letterCombinations(digits)
        execution_time = (time.time() - start_time) * 1000  # Convert to ms
        
        # Sort for consistent comparison
        result.sort()
        expected.sort()
        
        print(f"Test Case {i + 1}: digits = '{digits}' -> {result} {'✅' if result == expected else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")
