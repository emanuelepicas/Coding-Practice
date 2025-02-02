class Solution:
    # Solution 1: Iterative (Non-Recursive)
    def addDigits(self, num: int) -> int:
        """
        Iteratively add digits until we get a single digit
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        while num > 9:  # While number has more than one digit
            current_sum = 0
            # Add all digits
            while num:
                current_sum += num % 10  # Get last digit
                num //= 10               # Remove last digit
            num = current_sum
        return num
    
    # Solution 2: Recursive
    def addDigitsRecursive(self, num: int) -> int:
        """
        Recursively add digits until we get a single digit
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        """
        # Base case: if number is single digit
        if num < 10:
            return num
        
        # Calculate sum of digits
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
            
        # Recursively process the sum
        return self.addDigitsRecursive(digit_sum)
    
    # Solution 3: Mathematical (O(1) Follow-up)
    def addDigitsMath(self, num: int) -> int:
        """
        Using digital root formula
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if num == 0:
            return 0
        return 1 + ((num - 1) % 9)

def visualize_process(num: int):
    """
    Visualize how each solution processes the number
    """
    solution = Solution()
    
    print(f"\nProcessing number: {num}")
    
    # Iterative solution visualization
    print("\nIterative Solution:")
    temp = num
    while temp > 9:
        digits = []
        current_sum = 0
        n = temp
        while n:
            digits.append(n % 10)
            current_sum += n % 10
            n //= 10
        print(f"{temp} -> {' + '.join(map(str, digits))} = {current_sum}")
        temp = current_sum
    print(f"Final result: {temp}")
    
    # Recursive solution visualization
    print("\nRecursive Solution:")
    def recursive_visual(n, depth=0):
        if n < 10:
            print("  " * depth + f"Base case reached: {n}")
            return n
        
        digits = []
        digit_sum = 0
        temp = n
        while temp:
            digits.append(temp % 10)
            digit_sum += temp % 10
            temp //= 10
            
        print("  " * depth + f"{n} -> {' + '.join(map(str, digits))} = {digit_sum}")
        return recursive_visual(digit_sum, depth + 1)
    
    result = recursive_visual(num)
    print(f"Final result: {result}")
    
    # Mathematical solution
    math_result = solution.addDigitsMath(num)
    print(f"\nMathematical Solution (O(1)):")
    print(f"Result: {math_result}")

# Test cases
test_cases = [
    38,     # Example 1: 3 + 8 = 11, 1 + 1 = 2
    0,      # Example 2: Already single digit
    999,    # Multiple steps
    5,      # Already single digit
    123456  # Larger number
]

for test in test_cases:
    print("\n" + "="*50)
    visualize_process(test)