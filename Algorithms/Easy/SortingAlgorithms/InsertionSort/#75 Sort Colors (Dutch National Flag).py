class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort array containing only 0s, 1s, and 2s in-place
        Time: O(n)
        Space: O(1)
        """
        # Initialize pointers
        left = curr = 0    # left for 0s
        right = len(nums) - 1  # right for 2s
        
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

def visualize_sort_colors(nums):
    """Visualize the Dutch National Flag sorting process"""
    print(f"\nOriginal array: {nums}")
    
    left = curr = 0
    right = len(nums) - 1
    step = 1
    
    while curr <= right:
        print(f"\nStep {step}:")
        print(f"Current: {curr}, Left: {left}, Right: {right}")
        
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            print(f"Swapped 0 at position {curr} with {nums[curr]} at position {left}")
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            print(f"Swapped 2 at position {curr} with {nums[curr]} at position {right}")
            right -= 1
        else:
            print(f"Skipping 1 at position {curr}")
            curr += 1
            
        print(f"Current array: {nums}")
        step += 1
    
    print(f"\nFinal array: {nums}")