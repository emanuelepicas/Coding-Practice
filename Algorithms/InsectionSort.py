"""

Insertion Sort:
       - Best for small arrays (n < 50)
       - Good for nearly sorted arrays
       - In-place sorting (O(1) space)
       
Question: Implement insertion sort to sort an array in ascending order.
Visual explanation of how insertion sort works on array [5,2,4,1,3]:

Initial: [5,2,4,1,3]

Step 1: [2,5,4,1,3]  # 2 is inserted before 5
Step 2: [2,4,5,1,3]  # 4 is inserted between 2 and 5
Step 3: [1,2,4,5,3]  # 1 is inserted at the beginning
Step 4: [1,2,3,4,5]  # 3 is inserted between 2 and 4
"""

def insertion_sort(arr: list[int]) -> list[int]:
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        print(f"Current Value {key}")
        j = i - 1     # Index of the last element in sorted portion
        
        # Move elements that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        # Print each step for visualization
        print(f"Step {i}: {arr}")
    
    return arr

# Test Cases
test_cases = [
    [64, 34, 25, 12, 22, 11, 90],  # Random array
    [1, 2, 3, 4, 5],               # Already sorted
    [5, 4, 3, 2, 1],               # Reverse sorted
    [1],                           # Single element
    [],                            # Empty array
    [1, 1, 1, 1, 1]               # All same elements
]

for i, arr in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    print(f"Original array: {arr}")
    result = insertion_sort(arr.copy())
    print(f"Sorted array: {result}")
    print("-" * 40)