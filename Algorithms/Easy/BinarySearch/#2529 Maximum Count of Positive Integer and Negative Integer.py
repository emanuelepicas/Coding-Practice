class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        positive = 0
        negative = 0

        for i in nums:
            if i > 0:
                print(i)
                positive += 1
            elif i < 0:
                negative += 1
        
        return(max(positive, negative))