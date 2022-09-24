# link: https://leetcode.com/problems/longest-common-subsequence/

# Method 2: Top-Down DP with Memorization

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        
        def findLCM(i, j):
            
            if i == -1 or j == -1:
                return 0
            if LCM[i][j] != -1:
                return LCM[i][j]
            
            if text1[i] == text2[j]:
                LCM[i][j] = 1+findLCM(i-1, j-1)
            else:
                LCM[i][j] = max(findLCM(i-1, j), findLCM(i, j-1))
                
            return LCM[i][j]
        
        LCM = [[-1 for _ in range(n)] for _ in range(m)]
        
        return findLCM(m-1, n-1)

"""
Time Complexity: O(M*N)
Space Complexity: O(M*N)  
"""