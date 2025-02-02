# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            print(f"Current version of mid: {mid}")

            if isBadVersion(mid):
                right = mid
            else:
                left = mid +1
                print(f"Left is increasing {left}")
            
        return left
        