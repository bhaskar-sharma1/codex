class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x // 2
        ans = 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (4, 2),
        (8, 2),
        (0, 0),
        (1, 1),
        (9, 3),
        (16, 4),
        (25, 5),
        (26, 5),  # Non-perfect square test case
        (2147395599, 46339),  # Large test case (edge case)
    ]

    for x, expected in test_cases:
        output = solution.mySqrt(x)
        print(f"Input: {x} | Output: {output} {'✅' if output == expected else '❌'}")
