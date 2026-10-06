class Solution:
    def reverse(self, x: int) -> int:

        p = 0
        int_max=2**31-1
        int_min=-2**31

        is_negative = False
        if (x<0):
            is_negative = True
            x = abs(x)
        

        while x!=0:

            re = x%10
            x=  x//10

            if (p > int_max//10  or (p == int_max//10   and re > int_max%10)  ):
                return 0

            
            p = p*10 +re

        
        if is_negative:
            p = -p
        
        return p

            



        