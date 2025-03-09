class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0  # Edge case: Empty needle
        
        # Build LPS (Longest Prefix Suffix) array
        lps = [0] * len(needle)
        j = 0  # Pointer for LPS construction

        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
        
        # KMP Search
        j = 0  # Pointer for `needle`
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1  # Found the match
        
        return -1  # Needle not found

# Testing function locally
def test():
    solution = Solution()
    
    # Test Cases
    test_cases = [
        ("sadbutsad", "sad", 0),  # Expected output: 0
        ("leetcode", "leeto", -1),  # Expected output: -1
        ("hello", "ll", 2),  # Expected output: 2
        ("aaaaa", "bba", -1),  # Expected output: -1
        ("mississippi", "issip", 4)  # Expected output: 4
    ]

    # Run each test case
    for i, (haystack, needle, expected) in enumerate(test_cases, 1):
        result = solution.strStr(haystack, needle)
        print(f"Test Case {i}: {haystack}, {needle} -> {result} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()