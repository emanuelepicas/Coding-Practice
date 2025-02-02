class Solution:
    def countDigits(self, num: int) -> int:
        """
        Count digits in num that divide num evenly
        
        Time Complexity: O(log n) where n is num (number of digits)
        Space Complexity: O(1)
        """
        count = 0
        temp = num  # Store original number
        
        # Extract each digit and check if it divides num
        while temp > 0:
            digit = temp % 10  # Get last digit
            if digit != 0 and num % digit == 0:  # Check if digit divides num
                count += 1
            temp //= 10  # Remove last digit
            
        return count

def visualize_process(num: int):
    """
    Visualize how we check each digit
    """
    print(f"\nChecking number: {num}")
    print("Process:")
    
    count = 0
    temp = num
    digits = []
    
    # First extract all digits
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()  # Show digits in original order
    
    print(f"Digits in number: {digits}")
    
    # Check each digit
    for i, digit in enumerate(digits, 1):
        print(f"\nChecking digit {i}: {digit}")
        if digit == 0:
            print(f"{digit} is 0, skipping")
            continue
            
        if num % digit == 0:
            count += 1
            print(f"{num} ÷ {digit} = {num//digit} (divides evenly)")
            print(f"Count increased to {count}")
        else:
            print(f"{num} ÷ {digit} = {num/digit} (does not divide evenly)")
    
    print(f"\nFinal count: {count}")
    return count

# Test cases
test_cases = [
    7,      # Example 1
    121,    # Example 2
    1248,   # Example 3
    999,    # All same digits
    10,     # Two digits
    22,     # Power of 2
    100     # Contains zero
]

def run_tests():
    solution = Solution()
    
    for i, num in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}:")
        
        # Visualize the process
        expected = visualize_process(num)
        
        # Get solution result
        result = solution.countDigits(num)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got: {result}")
        assert result == expected, f"Test case failed! Expected {expected}, got {result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()