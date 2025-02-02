class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lenght = len(nums)
        """
        Find maximum average of contiguous subarray of length k
        using Sliding Window technique.
        
        Time Complexity: O(n) where n is length of nums
        Space Complexity: O(1)
        """
        # Initialize the sum of first k elements
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            # Add next element and remove first element of previous window
            curr_sum = curr_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)
            
        return max_sum / k

def test_max_average():
    solution = Solution()
    
    # Test cases with visualization
    test_cases = [
        {
            'nums': [1, 12, -5, -6, 50, 3],
            'k': 4,
            'expected': 12.75,
            'explanation': """
            Window size = 4
            Windows:
            [1, 12, -5, -6] = 2/4 = 0.5
            [12, -5, -6, 50] = 51/4 = 12.75 (maximum)
            [-5, -6, 50, 3] = 42/4 = 10.5
            """
        },
        {
            'nums': [5],
            'k': 1,
            'expected': 5.0,
            'explanation': """
            Window size = 1
            Only one window: [5] = 5.0
            """
        },
        {
            'nums': [1, 2, 3, 4, 5],
            'k': 3,
            'expected': 4.0,
            'explanation': """
            Window size = 3
            Windows:
            [1, 2, 3] = 6/3 = 2.0
            [2, 3, 4] = 9/3 = 3.0
            [3, 4, 5] = 12/3 = 4.0 (maximum)
            """
        },
        {
            'nums': [-1, -2, -3, -4, -5],
            'k': 2,
            'expected': -1.5,
            'explanation': """
            Window size = 2
            Windows:
            [-1, -2] = -3/2 = -1.5 (maximum)
            [-2, -3] = -5/2 = -2.5
            [-3, -4] = -7/2 = -3.5
            [-4, -5] = -9/2 = -4.5
            """
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        nums, k = case['nums'], case['k']
        expected = case['expected']
        
        print(f"\nTest Case {i}:")
        print(case['explanation'])
        
        # Calculate result
        result = solution.findMaxAverage(nums, k)
        
        # Print detailed information
        print(f"Input array: {nums}")
        print(f"Window size (k): {k}")
        print(f"Expected average: {expected}")
        print(f"Got average: {result}")
        
        # Verify result
        assert abs(result - expected) < 1e-5, f"Expected {expected}, but got {result}"
        print("✓ Test case passed")
        print("-" * 60)

def visualize_sliding_window():
    """
    Visualize how sliding window works on a sample array
    """
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    
    print("Sliding Window Visualization")
    print("=" * 60)
    print(f"Array: {nums}")
    print(f"Window size (k): {k}")
    print("\nSliding process:")
    
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    # Print initial window
    print("\nInitial window:")
    print([nums[i] for i in range(k)])
    print(f"Sum: {curr_sum}, Average: {curr_sum/k}")
    
    # Slide the window
    for i in range(k, len(nums)):
        removed = nums[i-k]
        added = nums[i]
        curr_sum = curr_sum + added - removed
        
        print(f"\nSlide window:")
        print(f"Removed: {removed}, Added: {added}")
        print([nums[j] for j in range(i-k+1, i+1)])
        print(f"Sum: {curr_sum}, Average: {curr_sum/k}")
        
        if curr_sum > max_sum:
            print("New maximum found!")
            max_sum = curr_sum

if __name__ == "__main__":
    print("Testing Maximum Average Subarray Solution\n")
    
    # Show sliding window visualization
    visualize_sliding_window()
    
    print("\nRunning Test Cases:")
    test_max_average()