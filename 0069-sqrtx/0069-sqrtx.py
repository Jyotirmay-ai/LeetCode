class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        ans =0

        while left<=right : 
            mid = left + (right - left) // 2

            if mid*mid == x:
                return mid

            elif  int (mid*mid) < x:
                left = mid + 1
                ans = mid
               
                
            elif int(mid * mid) > x:
                right = mid - 1
            
        return ans
                
            








