class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Calculate difference between sum of non-divisible and divisible numbers
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        num1 = sum(x for x in range(1, n + 1) if x % m != 0)  # Non-divisible sum
        num2 = sum(x for x in range(1, n + 1) if x % m == 0)  # Divisible sum
        return num1 - num2

    # Alternative solution using single pass
    def differenceOfSums_single_pass(self, n: int, m: int) -> int:
        not_divisible = 0
        divisible = 0
        for x in range(1, n + 1):
            if x % m == 0:
                divisible += x
            else:
                not_divisible += x
        return not_divisible - divisible

def visualize_process(n: int, m: int):
    """
    Visualize how we find and sum the numbers
    """
    print(f"\nProcessing range 1 to {n} with divisor {m}")
    
    # Find divisible and non-divisible numbers
    divisible = []
    not_divisible = []
    
    for i in range(1, n + 1):
        if i % m == 0:
            divisible.append(i)
            print(f"{i} is divisible by {m}")
        else:
            not_divisible.append(i)
            print(f"{i} is not divisible by {m}")
    
    # Calculate sums
    num1 = sum(not_divisible)
    num2 = sum(divisible)
    
    print(f"\nNumbers not divisible by {m}: {not_divisible}")
    print(f"Sum (num1): {' + '.join(map(str, not_divisible))} = {num1}")
    
    print(f"\nNumbers divisible by {m}: {divisible}")
    print(f"Sum (num2): {' + '.join(map(str, divisible)) if divisible else '0'} = {num2}")
    
    difference = num1 - num2
    print(f"\nDifference: {num1} - {num2} = {difference}")
    
    return difference

# Test cases
test_cases = [
    {
        'n': 10,
        'm': 3,
        'expected': 19,
        'description': "Example 1"
    },
    {
        'n': 5,
        'm': 6,
        'expected': 15,
        'description': "Example 2"
    },
    {
        'n': 5,
        'm': 1,
        'expected': -15,
        'description': "Example 3"
    },
    {
        'n': 7,
        'm': 2,
        'expected': 16,
        'description': "Even divisor"
    },
    {
        'n': 3,
        'm': 3,
        'expected': 3,
        'description': "Small range"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        n, m = case['n'], case['m']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_process(n, m)
        
        # Get solution results
        solution_result = solution.differenceOfSums(n, m)
        single_pass_result = solution.differenceOfSums_single_pass(n, m)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got (two pass): {solution_result}")
        print(f"Got (single pass): {single_pass_result}")
        assert solution_result == expected and single_pass_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}/{single_pass_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()