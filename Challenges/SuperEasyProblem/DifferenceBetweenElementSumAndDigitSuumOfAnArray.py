class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        """
        Calculate absolute difference between element sum and digit sum
        
        Time Complexity: O(n*m) where n is length of nums and m is max number of digits
        Space Complexity: O(1)
        """
        element_sum = sum(nums)  # Sum of all elements
        
        # Calculate digit sum
        digit_sum = 0
        for num in nums:
            while num > 0:
                digit_sum += num % 10  # Add last digit
                num //= 10            # Remove last digit
                
        return abs(element_sum - digit_sum)
    
    # Alternative solution using string conversion
    def differenceOfSum_string(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = sum(int(digit) for num in nums for digit in str(num))
        return abs(element_sum - digit_sum)

def visualize_process(nums: List[int]):
    """
    Visualize how we calculate both sums
    """
    print(f"\nProcessing array: {nums}")
    
    # Calculate element sum
    element_sum = sum(nums)
    print(f"\nElement Sum Calculation:")
    print(f"Sum of elements: {' + '.join(map(str, nums))} = {element_sum}")
    
    # Calculate digit sum
    print(f"\nDigit Sum Calculation:")
    digit_sum = 0
    for num in nums:
        digits = []
        temp = num
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10
        digits.reverse()  # Show digits in original order
        print(f"Number {num}: digits = {digits}")
        digit_sum += sum(digits)
        print(f"Running digit sum: {digit_sum}")
    
    # Calculate difference
    difference = abs(element_sum - digit_sum)
    print(f"\nFinal Calculation:")
    print(f"Element Sum: {element_sum}")
    print(f"Digit Sum: {digit_sum}")
    print(f"Absolute Difference: |{element_sum} - {digit_sum}| = {difference}")
    
    return difference

# Test cases
test_cases = [
    {
        'nums': [1,15,6,3],
        'expected': 9,
        'description': "Example 1"
    },
    {
        'nums': [1,2,3,4],
        'expected': 0,
        'description': "Example 2"
    },
    {
        'nums': [100,200,300],
        'expected': 594,
        'description': "Large numbers"
    },
    {
        'nums': [1],
        'expected': 0,
        'description': "Single number"
    },
    {
        'nums': [11,11,11],
        'expected': 27,
        'description': "Same numbers"
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
        result = visualize_process(nums)
        
        # Get solution result
        solution_result = solution.differenceOfSum(nums)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got: {solution_result}")
        assert solution_result == expected, \
            f"Test case failed! Expected {expected}, got {solution_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()