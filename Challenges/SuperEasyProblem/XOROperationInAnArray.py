class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Calculate XOR of array where nums[i] = start + 2 * i
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        for i in range(n):
            # Calculate current number and XOR with result
            num = start + 2 * i
            result ^= num
        return result
    
    # Alternative solution that generates array first (less space efficient)
    def xorOperation_with_array(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        return reduce(lambda x, y: x ^ y, nums)

def visualize_process(n: int, start: int):
    """
    Visualize how we generate the array and perform XOR operations
    """
    print(f"\nInput: n = {n}, start = {start}")
    
    # Generate array
    nums = []
    print("\nGenerating array:")
    for i in range(n):
        num = start + 2 * i
        nums.append(num)
        print(f"nums[{i}] = {start} + 2 * {i} = {num}")
    
    print(f"\nGenerated array: {nums}")
    
    # Perform XOR operations
    result = nums[0]
    print(f"\nXOR Operations:")
    print(f"Start with: {result}")
    
    for i in range(1, n):
        print(f"XOR with {nums[i]}: {result} ^ {nums[i]} = {result ^ nums[i]}")
        result ^= nums[i]
    
    print(f"\nFinal result: {result}")
    
    # Show binary representation
    print("\nBinary representation:")
    print(f"Result in binary: {bin(result)[2:].zfill(8)}")
    
    return result

# Test cases
test_cases = [
    {
        'n': 5,
        'start': 0,
        'expected': 8,
        'description': "Example 1"
    },
    {
        'n': 4,
        'start': 3,
        'expected': 8,
        'description': "Example 2"
    },
    {
        'n': 1,
        'start': 7,
        'expected': 7,
        'description': "Single element"
    },
    {
        'n': 10,
        'start': 5,
        'expected': 2,
        'description': "Larger array"
    },
    {
        'n': 3,
        'start': 0,
        'expected': 6,
        'description': "Start with zero"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        n, start = case['n'], case['start']
        expected = case['expected']
        
        # Visualize the process
        result = visualize_process(n, start)
        
        # Get solution result
        solution_result = solution.xorOperation(n, start)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got: {solution_result}")
        assert solution_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()