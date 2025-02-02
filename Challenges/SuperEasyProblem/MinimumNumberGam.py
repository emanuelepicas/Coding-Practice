class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        """
        Simulate Alice and Bob's number game
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) if we modify nums in-place
        """
        # Sort the array first to easily get minimum elements
        nums.sort()
        
        # Process pairs of numbers (since length is even)
        for i in range(0, len(nums)-1, 2):
            # three parameters, increment of two position in the third parameter
            # Swap adjacent elements (Alice's and Bob's numbers)
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums

def visualize_game(nums: List[int]):
    """
    Visualize how the game proceeds
    """
    print(f"\nStarting game with nums: {nums}")
    
    # Sort numbers
    sorted_nums = sorted(nums)
    print(f"Sorted array: {sorted_nums}")
    
    result = []
    i = 0
    round_num = 1
    
    while i < len(sorted_nums)-1:
        print(f"\nRound {round_num}:")
        # Alice's turn
        alice_min = sorted_nums[i]
        print(f"Alice removes minimum: {alice_min}")
        
        # Bob's turn
        bob_min = sorted_nums[i+1]
        print(f"Bob removes minimum: {bob_min}")
        
        # Append in reverse order (Bob then Alice)
        print(f"Bob appends: {bob_min}")
        result.append(bob_min)
        print(f"Alice appends: {alice_min}")
        result.append(alice_min)
        
        print(f"Current result: {result}")
        
        i += 2
        round_num += 1
    
    return result

# Test cases
test_cases = [
    [5,4,2,3],        # Example 1
    [2,5],            # Example 2
    [1,2,3,4],        # Sorted input
    [4,3,2,1],        # Reverse sorted
    [2,2,4,4]         # Duplicates
]

def run_tests():
    solution = Solution()
    
    for i, nums in enumerate(test_cases, 1):
        print("\n" + "="*50)
        print(f"Test Case {i}:")
        
        # Show game process
        result = visualize_game(nums.copy())
        print(f"\nVisualized result: {result}")
        
        # Get solution result
        solution_result = solution.numberGame(nums.copy())
        print(f"Solution result: {solution_result}")
        
        # Verify results match
        assert result == solution_result, f"Results don't match! {result} != {solution_result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()