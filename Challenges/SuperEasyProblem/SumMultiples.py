class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        Find sum of numbers from 1 to n that are divisible by 3, 5, or 7
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        return sum(x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)
    
    # Alternative solution using mathematical approach
    def sumOfMultiples_math(self, n: int) -> int:
        """
        Alternative solution using inclusion-exclusion principle
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        def sum_divisible_by(k: int) -> int:
            # Sum of numbers divisible by k from 1 to n
            p = n // k  # Count of numbers divisible by k
            return k * (p * (p + 1)) // 2
        
        # Include multiples of 3, 5, and 7
        result = sum_divisible_by(3) + sum_divisible_by(5) + sum_divisible_by(7)
        
        # Exclude numbers counted multiple times
        result -= sum_divisible_by(15)  # 3 * 5
        result -= sum_divisible_by(21)  # 3 * 7
        result -= sum_divisible_by(35)  # 5 * 7
        
        # Add back numbers counted three times
        result += sum_divisible_by(105)  # 3 * 5 * 7
        
        return result

def visualize_process(n: int):
    """
    Visualize how we find and sum the multiples
    """
    print(f"\nFinding multiples in range 1 to {n}:")
    
    multiples = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            multiples.append(i)
            print(f"\nNumber {i}:")
            reasons = []
            if i % 3 == 0: reasons.append("divisible by 3")
            if i % 5 == 0: reasons.append("divisible by 5")
            if i % 7 == 0: reasons.append("divisible by 7")
            print(f"Included because: {', '.join(reasons)}")
    
    total = sum(multiples)
    print(f"\nFound multiples: {multiples}")
    print(f"Sum: {' + '.join(map(str, multiples))} = {total}")
    
    return total

# Test cases
test_cases = [
    {
        'n': 7,
        'expected': 21,
        'description': "Example 1"
    },
    {
        'n': 10,
        'expected': 40,
        'description': "Example 2"
    },
    {
        'n': 9,
        'expected': 30,
        'description': "Example 3"
    },
    {
        'n': 15,
        'expected': 75,
        'description': "Larger number"
    },
    {
        'n': 2,
        'expected': 0,
        'description': "Small number"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        n = case['n']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_process(n)
        
        # Get solution results
        solution_result = solution.sumOfMultiples(n)
        math_result = solution.sumOfMultiples_math(n)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got (iterative): {solution_result}")
        print(f"Got (mathematical): {math_result}")
        assert solution_result == expected and math_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}/{math_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()