# link: https://leetcode.com/problems/coin-change/submissions/

# Method 2: Top-Down DP with Memorization

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def minCoin(i):
            
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            if ans[i] != -1:
                return ans[i]
            
            tmp = float("inf")
            for j in range(len(coins)):
                #if amount-coins[j] >= 0:
                tmp = min(tmp, 1 + minCoin(i-coins[j]))
            
            ans[i] = tmp
            return ans[i]
        
        ans = [-1]*(amount+1)
        output = minCoin(amount)

        if output >= float("inf"):
            return -1
        elif output == -1:
            return 0
        else:
            return output

"""
Recurrence Relation: ans(i) = min(ans, 1+climb(i-coin[j]))

Time Complexity: O(N)
Space Complexity: O(N)  
"""