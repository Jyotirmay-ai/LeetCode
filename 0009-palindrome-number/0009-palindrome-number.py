class Solution:
    def isPalindrome(self, x: int) -> bool:

        n=x
        p=0

        if (x <0):
            return False 
        
        if (x <10 ) :
            return True

        while n>0:

            r = n%10
            n = n//10
            p = p*10+r
                


        if(p == x):
            return True
        else:
            return False


        