class Solution:
     def reverse(self, x: int) -> int:
         n=0
         sign=-1 if x<0 else 1
         x=abs(x)
         while x!=0:
            n=n*10+x%10
            x=x//10
         if -2**31 > n  or n > 2**31 - 1:
            return 0
         return n*sign
