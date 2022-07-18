
# link: https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        low = 1
        high = x//2
        
        while low <= high:
            
            m = (low+high)//2
            
            if m*m < x:
                if (m+1)*(m+1) > x:
                    return m
                low = m+1
                
            elif m*m > x:
                high = m-1
            
            else:
                return m
                
        return 0