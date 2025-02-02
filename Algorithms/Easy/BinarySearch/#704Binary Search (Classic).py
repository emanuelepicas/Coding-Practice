class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #left, right = 0, len(nums) -1
        left, right = 0, len(nums)
        print(f"Lenght of the right {right}")
        steps = 0


        while left <= right:
            steps += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                print(f"The number {nums[mid]} in position {mid} is smaller ")
                left = mid + 1
            else:
                right = mid - 1
            
        return -1

