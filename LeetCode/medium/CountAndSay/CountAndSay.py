# Q38. Count and Say
import time
from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = "1"
        for _ in range(n - 1):
            current = []
            count = 1
            prev_char = result[0]
            # Process the current result string to generate the next sequence.
            for i in range(1, len(result)):
                if result[i] == prev_char:
                    count += 1
                else:
                    current.append(str(count))
                    current.append(prev_char)
                    count = 1
                    prev_char = result[i]
            # Append the last group.
            current.append(str(count))
            current.append(prev_char)
            result = "".join(current)
        
        return result

# --------------------------
# Testing function with execution time measurement
# For n = 1,4,5,10 we compare the full output.
# For n = 20 and n = 30, we only compare the prefix (since the full output is huge).
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, "1"),
        (4, "1211"),
        (5, "111221"),
        (10, "13211311123113112211"),
        (20, "111312211312111322212321121113121112131112132112311321322112"),
        (30, "311311222113111231133211121312211231131112311211133112111312")
    ]
    
    print("\n🔹 Running Test Cases with Execution Time & Verification:\n")
    
    for n, expected in test_cases:
        start_time = time.time()
        result = sol.countAndSay(n)
        execution_time = (time.time() - start_time) * 1000  # in ms
        
        # For n=20 and n=30, compare only the prefix (expected is a known prefix of the full string).
        if n in (20, 30):
            pass_fail = "✅" if result.startswith(expected) else "❌"
        else:
            pass_fail = "✅" if result == expected else "❌"
        
        # For readability, we show only the first 60 characters of the output.
        display_result = result[:60] + ("..." if len(result) > 60 else "")
        
        print(f"Test Case: n = {n}")
        print(f"Output (prefix): {display_result}")
        print(f"Execution Time: {execution_time:.4f} ms")
        print(f"Result: {pass_fail}\n")
