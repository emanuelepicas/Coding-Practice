class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Sort array so that nums[0] <= nums[1] >= nums[2] <= nums[3]...
        Time: O(n)
        Space: O(1)
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or \
               (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

def visualize_wiggle_sort(nums):
    """Visualize the wiggle sort process"""
    print(f"\nOriginal array: {nums}")
    
    for i in range(len(nums) - 1):
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or \
           (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(f"\nStep {i+1}:")
            print(f"Swapped positions {i} and {i+1}")
            print(f"Current array: {nums}")
    
    print(f"\nFinal array: {nums}")