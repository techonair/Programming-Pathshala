# link: https://leetcode.com/problems/edit-distance/

# Method 2: Top-Down DP with Memorization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        
        def edit(i, j):
            
            if i == -1:
                # insert all elements of word2 into word1=""
                return j+1
            if j == -1:
                # delete all elements of word1 as word2=""
                return i+1
            if ans[i][j] != -1:
                return ans[i][j]
            
            if word1[i] == word2[j]:
                ans[i][j] = edit(i-1, j-1)
            else:
                # element of choices: insert, delete, replace
                ans[i][j] = 1+min(
                                  edit(i,j-1),
                                  edit(i-1,j),
                                  edit(i-1,j-1)
                                  )
                
            return ans[i][j]
        
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        
        return edit(m-1, n-1)  

"""
Time Complexity: O(M*N)
Space Complexity: O(M*N)  
"""       