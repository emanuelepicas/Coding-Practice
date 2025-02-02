class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        """
        Find next greater element using monotonic stack
        
        Time Complexity: O(n) where n is length of nums2
        Space Complexity: O(n) for the stack and hashmap
        """
        # Dictionary to store next greater element for each number
        next_greater = {}
        # Monotonic decreasing stack
        stack = []
        
        # Process nums2 to find next greater element for each number
        for num in nums2:
            # While stack has elements and current number is greater than top
            while stack and num > stack[-1]:
                # Current number is the next greater element for top of stack
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # For remaining elements in stack, no greater element exists
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build result for nums1 using the dictionary
        return [next_greater[num] for num in nums1]

def visualize_process(nums1, nums2) -> None:
    """Visualize how the monotonic stack works"""
    next_greater = {}
    stack = []
    
    print(f"nums1: {nums1}")
    print(f"nums2: {nums2}")
    print("\nProcessing nums2 with monotonic stack:")
    
    for i, num in enumerate(nums2):
        print(f"\nStep {i + 1}:")
        print(f"Current number: {num}")
        print(f"Stack before: {stack}")
        
        while stack and num > stack[-1]:
            popped = stack.pop()
            next_greater[popped] = num
            print(f"Found next greater element: {popped} -> {num}")
            print(f"Stack after pop: {stack}")
        
        stack.append(num)
        print(f"Stack after push: {stack}")
        print(f"Current next_greater map: {next_greater}")
    
    # Handle remaining elements in stack
    print("\nProcessing remaining elements in stack:")
    while stack:
        popped = stack.pop()
        next_greater[popped] = -1
        print(f"No greater element for {popped}")
    
    # Build result
    result = [next_greater[num] for num in nums1]
    print(f"\nFinal next_greater map: {next_greater}")
    print(f"Result for nums1: {result}")

# Test cases
test_cases = [
    {
        'nums1': [4,1,2],
        'nums2': [1,3,4,2],
        'expected': [-1,3,-1],
        'description': "Example 1 from problem"
    },
    {
        'nums1': [2,4],
        'nums2': [1,2,3,4],
        'expected': [3,-1],
        'description': "Example 2 from problem"
    },
    {
        'nums1': [1,3,5,2,4],
        'nums2': [6,5,4,3,2,1,7],
        'expected': [7,7,7,7,7],
        'description': "Additional test case"
    },{
        'nums1': [1],
        'nums2': [1,5,3,4,2],
        'expected': [2],
        'description': "Additional test case"
    }]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {case['description']}")
        print("=" * 50)
        
        nums1, nums2 = case['nums1'], case['nums2']
        expected = case['expected']
        
        # Visualize the process
        visualize_process(nums1, nums2)
        
        # Get actual result
        result = solution.nextGreaterElement(nums1, nums2)
        
        # Verify result
        print(f"\nExpected: {expected}")
        print(f"Got: {result}")
        assert result == expected, f"Test case failed! Expected {expected}, got {result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()