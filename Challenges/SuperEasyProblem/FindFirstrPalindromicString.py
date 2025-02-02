class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Find first palindromic string in array
        
        Time Complexity: O(n*m) where n is length of words array and m is max word length
        Space Complexity: O(1)
        """
        # Check each word
        for word in words:
            # Check if word is palindrome using two-pointer technique
            if word == word[::-1]:
                return word
        return ""

    # Alternative solution with helper function
    def firstPalindrome_verbose(self, words: List[str]) -> str:
        def isPalindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""

def visualize_process(words: List[str]):
    """
    Visualize how we check each word for palindrome
    """
    print(f"\nChecking words: {words}")
    print("\nProcess:")
    
    for i, word in enumerate(words, 1):
        print(f"\nWord {i}: '{word}'")
        print(f"Reversed: '{word[::-1]}'")
        
        # Check if palindrome
        if word == word[::-1]:
            print(f"✓ '{word}' is palindromic!")
            return word
        else:
            print(f"✗ '{word}' is not palindromic")
    
    print("\nNo palindromic strings found")
    return ""

# Test cases
test_cases = [
    ["abc","car","ada","racecar","cool"],  # Example 1
    ["notapalindrome","racecar"],          # Example 2
    ["def","ghi"],                         # Example 3
    ["a","b","c"],                         # Single letters
    ["radar","level","hello"],             # Multiple palindromes
    [""],                                  # Empty string
    ["aa","bb","cc"]                       # Two-letter palindromes
]

def run_tests():
    solution = Solution()
    
    for i, words in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}:")
        
        # Visualize the process
        expected = visualize_process(words)
        
        # Get solution result
        result = solution.firstPalindrome(words)
        
        # Verify results
        print(f"\nExpected: '{expected}'")
        print(f"Got: '{result}'")
        assert result == expected, f"Test case failed! Expected '{expected}', got '{result}'"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()