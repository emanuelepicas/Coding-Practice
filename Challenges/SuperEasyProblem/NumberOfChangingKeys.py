class Solution:
    def countKeyChanges(self, s: str) -> int:
        """
        Count number of key changes in string
        Ignores case when comparing consecutive characters
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(1)
        """
        if len(s) <= 1:
            return 0
            
        changes = 0
        # Compare adjacent characters (case-insensitive)
        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                changes += 1
                
        return changes
    
    # Alternative solution using zip
    def countKeyChanges_zip(self, s: str) -> int:
        return sum(1 for a, b in zip(s, s[1:]) 
                  if a.lower() != b.lower())

def visualize_process(s: str):
    """
    Visualize how we count key changes
    """
    print(f"\nAnalyzing string: '{s}'")
    print("Process:")
    
    changes = 0
    for i in range(1, len(s)):
        prev_char = s[i-1]
        curr_char = s[i]
        
        print(f"\nComparing: {prev_char} → {curr_char}")
        print(f"Lower case: {prev_char.lower()} → {curr_char.lower()}")
        
        if curr_char.lower() != prev_char.lower():
            changes += 1
            print(f"Key change detected! Count: {changes}")
        else:
            print("No key change (same letter or just case change)")
    
    print(f"\nTotal key changes: {changes}")
    return changes

# Test cases
test_cases = [
    {
        's': "aAbBcC",
        'expected': 2,
        'description': "Example 1"
    },
    {
        's': "AaAaAaA",
        'expected': 0,
        'description': "Example 2 - No changes"
    },
    {
        's': "abcde",
        'expected': 4,
        'description': "All different letters"
    },
    {
        's': "a",
        'expected': 0,
        'description': "Single character"
    },
    {
        's': "AbAbA",
        'expected': 0,
        'description': "Alternating case"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        s = case['s']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_process(s)
        
        # Get solution results
        solution_result = solution.countKeyChanges(s)
        zip_result = solution.countKeyChanges_zip(s)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got (regular): {solution_result}")
        print(f"Got (zip): {zip_result}")
        assert solution_result == expected and zip_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}/{zip_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()