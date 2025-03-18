import time

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Result array to hold the multiplication result
        res = [0] * (len(num1) + len(num2))

        # Reverse both numbers for easier calculation
        num1, num2 = num1[::-1], num2[::-1]

        # Perform multiplication digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10  # Carry to the next position
                res[i + j] %= 10

        # Remove leading zeros
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # Join the result array into string and reverse it
        return ''.join(map(str, res[::-1]))

# Test Cases
TEST_CASES = [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("0", "0", "0"),
    ("1", "1", "1"),
    ("999", "999", "998001"),
    ("123456789", "987654321", "121932631112635269"),
]

if __name__ == "__main__":

    solution = Solution()
    for num1, num2, expected in TEST_CASES:
        start_time = time.time()
        result = solution.multiply(num1, num2)
        execution_time = (time.time() - start_time) * 1000
        print(f"Test Case: num1 = {num1}, num2 = {num2}\nOutput: {result} {'✅' if result == expected else '❌'}")
        print(f"Execution Time: {execution_time:.4f} ms\n")