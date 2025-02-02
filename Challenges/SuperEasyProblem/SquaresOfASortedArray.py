class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach to get squares in sorted order
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        # Fill result array from end to start
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
                
        return result
    
    # Simple but less efficient solution
    def sortedSquares_simple(self, nums: List[int]) -> List[int]:
        """
        Simple approach: square and sort
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        return sorted(x * x for x in nums)

def visualize_process(nums: List[int]):
    """
    Visualize how we create sorted squares array
    """
    print(f"\nProcessing array: {nums}")
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    
    print("\nTwo-pointer approach:")
    for i in range(n - 1, -1, -1):
        left_val = abs(nums[left])
        right_val = abs(nums[right])
        
        print(f"\nStep {n-i}:")
        print(f"Comparing |{nums[left]}| = {left_val} and |{nums[right]}| = {right_val}")
        
        if left_val > right_val:
            square = nums[left] * nums[left]
            print(f"Left value larger: {nums[left]}² = {square}")
            result[i] = square
            left += 1
        else:
            square = nums[right] * nums[right]
            print(f"Right value larger: {nums[right]}² = {square}")
            result[i] = square
            right -= 1
            
        print(f"Current result: {result}")
    
    return result

# Test cases
test_cases = [
    {
        'nums': [-4,-1,0,3,10],
        'expected': [0,1,9,16,100],
        'description': "Example 1"
    },
    {
        'nums': [-7,-3,2,3,11],
        'expected': [4,9,9,49,121],
        'description': "Example 2"
    },
    {
        'nums': [0,1,2,3,4],
        'expected': [0,1,4,9,16],
        'description': "All positive"
    },
    {
        'nums': [-4,-3,-2,-1],
        'expected': [1,4,9,16],
        'description': "All negative"
    },
    {
        'nums': [-2,-1,0,1,2],
        'expected': [0,1,1,4,4],
        'description': "Centered around zero"
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
        result = visualize_process(nums.copy())
        
        # Get solution results
        solution_result = solution.sortedSquares(nums.copy())
        simple_result = solution.sortedSquares_simple(nums.copy())
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got (optimized): {solution_result}")
        print(f"Got (simple): {simple_result}")
        assert solution_result == expected and simple_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}/{simple_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()