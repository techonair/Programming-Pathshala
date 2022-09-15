"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def count(x):
            c = 0
            i = n-1
            j = 0
            
            while i >= 0 and j < n:
                if matrix[i][j] > x:
                    i -= 1
                else:
                    c += i+1
                    j += 1
            return c
           
        
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        while low <= high:
            m = (low+high)//2
            cnt = count(m)
            if cnt < k:
                low = m + 1
            else:
                cnt1 = count(m-1)
                if cnt1 < k:
                    return m
                high = m-1
        return 0
    """
        
""" 
Incomplete Code for count
           for i in range(n):
                low = 0
                high = n-1

                while low <= high:
                    mid = (low+high)//2

                    if matrix[i][mid] <= x:
                        low = mid+1
                    else:
                        if mid == 0 and matrix[i][mid] 
                        if mid > 0 and matrix[i][mid] > x and matrix[i][mid-1] > x:
                            high = mid-1
                        else:
                            c +=  mid  
            return c"""

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
def kthSmallest(matrix, k):
    
    m = len(matrix)
    n = len(matrix[0])
    
    def count(x):
        c = 0
        l = 0
        h = n-1
        
        while l<=h:
            mid = (l+h)//2
            if matrix[l][mid] > x:
                h -= 1
            else:
                c += l+1
                l += 1
        return c
        
    
    low = matrix[0][0]
    high = matrix[n-1][n-1]
    
    while low <= high:
        m = (low+high)//2
        cnt = count(m)
        if cnt < k:
            low = m + 1
        else:
            cnt1 = count(m-1)
            if cnt1 < k:
                return m
            high = m-1
    return 0           

print(kthSmallest(matrix, k))