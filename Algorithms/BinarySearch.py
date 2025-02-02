"""
Binary Search Algorithm Implementation

Time Complexity: O(log n)
- The search space is halved in each step
- For n elements, it takes log₂(n) steps to find the target

Space Complexity: O(1) for iterative, O(log n) for recursive
- Iterative: Uses only a constant amount of extra space
- Recursive: Uses call stack space proportional to log n

Example:
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 7

Step 1: mid = 3, arr[3] = 7 (Found!)
[1, 3, 5, 7, 9, 11, 13, 15]
         ↑
"""

from typing import List, Optional
import time

class BinarySearch:
    def iterative_search(self, arr: List[int], target: int) -> int:
        """
        Iterative implementation of binary search.
        Returns index of target if found, -1 otherwise.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        print(f"Lenght of the right {right}")
        steps = 0
        
        while left <= right:
            steps += 1
            mid = (left + right) // 2
            print(f"\nStep {steps}:")
            print(self._visualization(arr, left, mid, right, target))
            
            if arr[mid] == target:
                print(f"\nFound {target} at index {mid} in {steps} steps")
                return mid
            elif arr[mid] < target:
                left = mid + 1
                print("Target is in right half")
            else:
                right = mid - 1
                print("Target is in left half")
        
        print(f"\nTarget {target} not found after {steps} steps")
        return -1

    def recursive_search(self, arr: List[int], target: int, 
                        left: int = 0, right: Optional[int] = None, steps: int = 0) -> int:
        """
        Recursive implementation of binary search.
        Returns index of target if found, -1 otherwise.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursive call stack
        """
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            print(f"\nTarget {target} not found after {steps} steps")
            return -1
        
        steps += 1
        mid = (left + right) // 2
        print(f"\nStep {steps}:")
        print(self._visualization(arr, left, mid, right, target))
        
        if arr[mid] == target:
            print(f"\nFound {target} at index {mid} in {steps} steps")
            return mid
        elif arr[mid] < target:
            print("Target is in right half")
            return self.recursive_search(arr, target, mid + 1, right, steps)
        else:
            print("Target is in left half")
            return self.recursive_search(arr, target, left, mid - 1, steps)

    def _visualization(self, arr: List[int], left: int, mid: int, right: int, target: int) -> str:
        """Helper function to visualize the binary search process."""
        result = []
        for i, num in enumerate(arr):
            if i == mid:
                result.append(f"[{num}]")  # Current middle element
            elif left <= i <= right:
                result.append(f" {num} ")  # Current search range
            else:
                result.append(f"({num})")  # Outside search range
        
        visual = " ".join(result)
        status = f"\nSearch range: {left} to {right}"
        status += f"\nMiddle index: {mid}, Middle value: {arr[mid]}"
        status += f"\nTarget: {target}"
        
        return visual + status

def performance_test(func, arr: List[int], target: int) -> float:
    """Measure execution time of search function."""
    start_time = time.time()
    func(arr, target)
    end_time = time.time()
    return end_time - start_time

def run_tests():
    bs = BinarySearch()
    
    # Test cases
    test_cases = [
        {
            'arr': [1, 3, 5, 7, 9, 11, 13, 15],
            'targets': [7, 15, 1, 10],  # middle, end, start, not found
            'description': 'Basic test with even length array'
        },
        {
            'arr': [2, 4, 6, 8, 10],
            'targets': [6, 1],  # middle, not found
            'description': 'Basic test with odd length array'
        },
        {
            'arr': list(range(0, 100, 2)),  # [0,2,4,...,98]
            'targets': [48, 99],  # found, not found
            'description': 'Large array test'
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case['description']}")
        print("=" * 60)
        
        arr = test_case['arr']
        for target in test_case['targets']:
            print(f"\nSearching for target: {target}")
            print("\nIterative Binary Search:")
            iterative_time = performance_test(
                lambda x, y: bs.iterative_search(x, y), arr, target
            )
            
            print("\nRecursive Binary Search:")
            recursive_time = performance_test(
                lambda x, y: bs.recursive_search(x, y), arr, target
            )
            
            print(f"\nPerformance Comparison:")
            print(f"Iterative Time: {iterative_time:.6f} seconds")
            print(f"Recursive Time: {recursive_time:.6f} seconds")
            print("-" * 60)

if __name__ == "__main__":
    run_tests()