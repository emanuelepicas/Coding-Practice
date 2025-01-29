"""
Question: Implement merge sort to sort an array in ascending order.
Visual explanation of how merge sort works on array [38,27,43,3,9,82,10]:

                [38,27,43,3,9,82,10]
                /                \
        [38,27,43,3]        [9,82,10]
         /        \          /       \
    [38,27]    [43,3]    [9,82]    [10]
     /    \     /    \    /    \     |
  [38]   [27] [43]  [3] [9]   [82] [10]
     \    /     \    /    \    /     |
    [27,38]    [3,43]    [9,82]    [10]
         \        /          \       /
        [3,27,38,43]        [9,10,82]
                \                /
            [3,9,10,27,38,43,82]
"""

def merge_sort(arr: list[int]) -> list[int]:
    # Print the current state
    print(f"Splitting: {arr}")
    
    # Base case: if array has 1 or fewer elements, it's sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array, if any
    result.extend(left[i:])
    
    # Add remaining elements from right array, if any
    result.extend(right[j:])
    
    print(f"Merging: {result}")
    return result

# Test Cases with Detailed Visualization
test_cases = [
    [38, 27, 43, 3, 9, 82, 10],    # Random array
    [1, 2, 3, 4, 5],               # Already sorted
    [5, 4, 3, 2, 1],               # Reverse sorted
    [1],                           # Single element
    [],                            # Empty array
    [1, 1, 1, 1, 1]               # All same elements
]

# Function to run test cases
def test_merge_sort():
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Original array: {arr}")
        print("\nSorting Process:")
        result = merge_sort(arr.copy())
        print(f"\nFinal sorted array: {result}")
        print("-" * 60)

# Comparison of All Sorting Algorithms
def compare_sorting_algorithms():
    """
    Compare insertion sort, merge sort, and quick sort
    """
    from time import time
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    test_array = [38, 27, 43, 3, 9, 82, 10] * 100  # Larger array for better comparison
    
    # Test Insertion Sort
    start = time()
    insertion_result = insertion_sort(test_array.copy())
    insertion_time = time() - start
    
    # Test Merge Sort
    start = time()
    merge_result = merge_sort(test_array.copy())
    merge_time = time() - start
    
    # Test Quick Sort
    start = time()
    quick_result = quick_sort(test_array.copy())
    quick_time = time() - start
    
    print("\nPerformance Comparison:")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")

if __name__ == "__main__":
    print("Testing Insertion Sort:")
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Original array: {arr}")
        result = insertion_sort(arr.copy())
        print(f"Final sorted array: {result}")
        print("-" * 40)
    
    print("\nTesting Merge Sort:")
    test_merge_sort()
    
    print("\nComparing All Sorting Algorithms:")
    compare_sorting_algorithms()