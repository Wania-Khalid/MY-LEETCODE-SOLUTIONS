class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 1  # ways to reach step 1
        prev2 = 2  # ways to reach step 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        
        return prev2
        
        