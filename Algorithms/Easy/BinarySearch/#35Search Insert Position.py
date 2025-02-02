class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      left, right = 0, len(nums)

      while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
        # the iteration will start from the mid because the nums[mid is bigger]
      return left 
     