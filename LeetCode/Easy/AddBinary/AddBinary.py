class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        result = ""

        while i >= 0 or j >= 0 or carry:
            sum_ = carry
            if i >= 0:
                sum_ += int(a[i])
                i -= 1
            if j >= 0:
                sum_ += int(b[j])
                j -= 1
            carry = sum_ // 2
            result = str(sum_ % 2) + result  # Directly prepend instead of reversing

        return result

if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("1111", "1111", "11110"),
        ("0", "0", "0"),
        ("100", "11001", "11101"),
        ("1", "111", "1000"),
        ("110", "110", "1100"),
        ("111111", "1", "1000000"),  # Edge case with carry overflow
        ("10101", "0", "10101"),     # Adding zero should return the same number
        ("0", "1111", "1111"),       # Adding zero to a number
    ]
    for a, b, expected in test_cases:
        output = solution.addBinary(a, b)
        print(f"Input: '{a} ' + '{b}' | Output: '{output}' {'✅' if output == expected else '❌'}")