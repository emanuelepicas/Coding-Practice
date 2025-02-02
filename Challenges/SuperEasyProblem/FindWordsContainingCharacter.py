class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Find indices of words containing character x
        
        Time Complexity: O(n*m) where n is length of words and m is max word length
        Space Complexity: O(k) where k is number of matching words
        """
        return [i for i, word in enumerate(words) if x in word]
    
    # Alternative more verbose solution
    def findWordsContaining_verbose(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result

def visualize_search(words: List[str], x: str):
    """
    Visualize how we search for character in words
    """
    print(f"\nSearching for character '{x}' in words: {words}")
    print("\nProcess:")
    
    result = []
    for i, word in enumerate(words):
        print(f"\nChecking word {i}: '{word}'")
        
        if x in word:
            # Show where character appears
            positions = [pos for pos, char in enumerate(word) if char == x]
            print(f"Found '{x}' at position(s): {positions}")
            result.append(i)
            print(f"Added index {i} to result")
        else:
            print(f"'{x}' not found in word")
    
    print(f"\nFinal result indices: {result}")
    return result

# Test cases
test_cases = [
    {
        'words': ["leet","code"],
        'x': "e",
        'expected': [0,1],
        'description': "Example 1 - Character in both words"
    },
    {
        'words': ["abc","bcd","aaaa","cbc"],
        'x': "a",
        'expected': [0,2],
        'description': "Example 2 - Character in some words"
    },
    {
        'words': ["abc","bcd","aaaa","cbc"],
        'x': "z",
        'expected': [],
        'description': "Example 3 - Character in no words"
    },
    {
        'words': ["aaa","aaa","aaa"],
        'x': "a",
        'expected': [0,1,2],
        'description': "Character in all words"
    },
    {
        'words': ["xyz"],
        'x': "y",
        'expected': [0],
        'description': "Single word"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        words = case['words']
        x = case['x']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_search(words, x)
        
        # Get solution results
        solution_result = solution.findWordsContaining(words, x)
        verbose_result = solution.findWordsContaining_verbose(words, x)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got (concise): {solution_result}")
        print(f"Got (verbose): {verbose_result}")
        assert sorted(solution_result) == sorted(expected) and \
               sorted(verbose_result) == sorted(expected), \
            f"Test case failed! Expected {expected}, got {solution_result}/{verbose_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()