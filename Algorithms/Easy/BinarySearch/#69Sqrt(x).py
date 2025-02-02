class Solution:
    def mySqrt(self, x: int) -> int:
        

        if x < 2:
            return x

        left, right = 1 , x // 2

        while left <= right:
            mid = (left + right) // 2
            print(f"current mid {mid}")
            square = mid * mid
            print(f"Current square {square}")

            if square == x:
                return mid

            elif square < x:
                left = mid + 1
            
            else:
                right = mid - 1

        return right