class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr
    
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
        (20, 10946),
        (30, 1346269),
        (45, 1836311903),  # Edge case: Maximum constraint
    ]

    for n, expected in test_cases:
        output = solution.climbStairs(n)
        print(f"Input: {n} | Output: {output} {'✅' if output == expected else '❌'}")