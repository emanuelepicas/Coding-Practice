class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(arr)

        max_sum = float('-inf')

        for i in range(n - k + 1):
            current_sum = 0