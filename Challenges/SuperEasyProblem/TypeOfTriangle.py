class Solution:
    def triangleType(self, nums: List[int]) -> str:
        """
        Determine type of triangle based on side lengths
        
        Time Complexity: O(1) as array is always size 3
        Space Complexity: O(1)
        """
        # Check if it can form a triangle
        a, b, c = nums
        if a + b <= c or b + c <= a or a + c <= b:
            return "none"
        
        # Count unique sides
        unique_sides = len(set(nums))
        
        # Determine triangle type
        if unique_sides == 1:
            return "equilateral"
        elif unique_sides == 2:
            return "isosceles"
        else:
            return "scalene"

def visualize_triangle_check(nums: List[int]):
    """
    Visualize the process of checking triangle type
    """
    print(f"\nAnalyzing sides: {nums}")
    a, b, c = nums
    
    # Check triangle inequality
    print("\nChecking triangle inequality:")
    print(f"{a} + {b} = {a+b} {'>' if a+b > c else '<='} {c}")
    print(f"{b} + {c} = {b+c} {'>' if b+c > a else '<='} {a}")
    print(f"{a} + {c} = {a+c} {'>' if a+c > b else '<='} {b}")
    
    if a + b <= c or b + c <= a or a + c <= b:
        print("\nCannot form a triangle!")
        return "none"
    
    # Count unique sides
    unique_sides = len(set(nums))
    print(f"\nNumber of unique sides: {unique_sides}")
    
    # Determine type
    if unique_sides == 1:
        print("All sides equal → Equilateral")
        return "equilateral"
    elif unique_sides == 2:
        print("Two sides equal → Isosceles")
        return "isosceles"
    else:
        print("All sides different → Scalene")
        return "scalene"

# Test cases
test_cases = [
    {
        'nums': [3,3,3],
        'expected': "equilateral",
        'description': "Example 1 - Equilateral triangle"
    },
    {
        'nums': [3,4,5],
        'expected': "scalene",
        'description': "Example 2 - Scalene triangle"
    },
    {
        'nums': [3,3,4],
        'expected': "isosceles",
        'description': "Isosceles triangle"
    },
    {
        'nums': [1,1,3],
        'expected': "none",
        'description': "Cannot form triangle"
    },
    {
        'nums': [2,2,2],
        'expected': "equilateral",
        'description': "Another equilateral"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        nums = case['nums']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_triangle_check(nums)
        
        # Get solution result
        solution_result = solution.triangleType(nums)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got: {solution_result}")
        assert solution_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()