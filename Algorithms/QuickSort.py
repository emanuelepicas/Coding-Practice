"""
Quick Sort:
       - Best average-case performance
       - In-place version available
       - Performance depends on pivot selection
"""

def quick_sort(arr: list[int], depth: int = 0) -> list[int]:
    # Add depth parameter to track recursion level for visualization
    indent = "    " * depth  # Indentation for visual clarity
    
    print(f"{indent}Sorting array: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Array of length <= 1, returning: {arr}")
        return arr
    
    # Choose middle element as pivot
    pivot = arr[len(arr)//2]
    print(f" I want to see the result {arr[len(arr) // 2]}")
    print(f"{indent}Chosen pivot: {pivot}")
    
    # Short way of creating a partition of an array
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}Left partition: {left}")
    print(f"{indent}Middle partition: {middle}")
    print(f"{indent}Right partition: {right}")
    
    # Recursively sort left and right partitions
    print(f"{indent}Recursively sorting left partition...")
    sorted_left = quick_sort(left, depth + 1)
    print(f"{indent}Recursively sorting right partition...")
    sorted_right = quick_sort(right, depth + 1)
    
    # Combine results
    result = sorted_left + middle + sorted_right
    print(f"{indent}Combining: {sorted_left} + {middle} + {sorted_right}")
    print(f"{indent}Result: {result}")
    
    return result

def test_quick_sort():
    # Test cases with visual explanation
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],  # Random array
        [5, 4, 3, 2, 1],           # Reverse sorted
        [1, 2, 3, 4, 5],           # Already sorted
        [1],                       # Single element
        [],                        # Empty array
        [1, 1, 1, 1]              # All same elements
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Original array: {arr}")
        print("\nQuick Sort Process:")
        result = quick_sort(arr.copy())
        print(f"\nFinal sorted array: {result}")
        print("=" * 60)

# Visual example with detailed steps
def visual_quick_sort_example():
    """
    Visual representation of Quick Sort working on array [3,1,4,1,5,9,2,6]
    """
    print("""
Quick Sort Visual Example:
Initial array: [3,1,4,1,5,9,2,6]

Step 1: Choose pivot (4)
[3,1,4,1,5,9,2,6]
Partition into:
Left (< 4):  [3,1,1,2]
Middle (= 4): [4]
Right (> 4): [5,9,6]

Step 2a: Sort left partition [3,1,1,2]
Choose pivot (1)
Left (< 1):  []
Middle (= 1): [1,1]
Right (> 1): [3,2]

Step 2b: Sort [3,2]
Choose pivot (2)
Left (< 2):  []
Middle (= 2): [2]
Right (> 2): [3]

Step 2c: Combine left partition
Result: [1,1,2,3]

Step 3a: Sort right partition [5,9,6]
Choose pivot (9)
Left (< 9):  [5,6]
Middle (= 9): [9]
Right (> 9): []

Step 3b: Sort [5,6]
Choose pivot (5)
Left (< 5):  []
Middle (= 5): [5]
Right (> 5): [6]

Step 3c: Combine right partition
Result: [5,6,9]

Final Step: Combine all partitions
[1,1,2,3] + [4] + [5,6,9]
Result: [1,1,2,3,4,5,6,9]
    """)

if __name__ == "__main__":
    print("Quick Sort Algorithm Visualization\n")
    
    # Show detailed visual example
    visual_quick_sort_example()
    
    print("\nRunning Test Cases with Step-by-Step Visualization:")
    test_quick_sort()