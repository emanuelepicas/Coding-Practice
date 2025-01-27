from typing import List
import time

class Solution:
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force solution with O(n²) time complexity
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        Hash map solution with O(n) time complexity
        """
        seen = {}  # Hash map to store number:index pairs
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []  # No solution found

def test_solution(nums: List[int], target: int, solution_func) -> None:
    """
    Test helper function to run and time the solutions
    """
    start_time = time.time()
    result = solution_func(nums, target)
    end_time = time.time()
    
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Time taken: {(end_time - start_time)*1000:.4f} ms")
    
    # Verify the solution
    if result:
        print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {target}")
    print("-" * 50)

def main():
    # Create instance of Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 8, 3, 9, 2, 7], 10),  # Larger test case
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19),  # Even larger test case
    ]
    
    print("Testing Brute Force Solution:")
    print("=" * 50)
    for nums, target in test_cases:
        test_solution(nums, target, solution.twoSum_brute_force)
    
    print("\nTesting Hash Map Solution:")
    print("=" * 50)
    for nums, target in test_cases:
        test_solution(nums, target, solution.twoSum_hashmap)


if __name__ == "__main__":
    main()