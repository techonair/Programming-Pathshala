# link: https://leetcode.com/problems/min-cost-climbing-stairs

# Method 1: Brute Force (Using Inclusion & Exclusion Principle)
# Output for big inputs: Time Limit Exceeded

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(step, totalCost):
            
            nonlocal minCost
            
            if step == len(cost)-1:
                minCost = min(minCost, totalCost+cost[step])
                return
            
            if step == len(cost):
                minCost = min(minCost, totalCost)
                return
            
            climb(step+1, totalCost+cost[step])
            climb(step+2, totalCost+cost[step])
        
        i = 0
        j = 1
        minCost = float("inf")
        totalCost = 0
        
        climb(i, totalCost)
        climb(j, totalCost)
        
        return minCost

# Method 1.1: Brute Force Using Recurrence Relation
# TLE

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(step):
            
            if step < 0:
                return 0
            if step == 0 or step == 1:
                return cost[step]
            
            return cost[step] + min(climb(step-1), climb(step-2))
        
        n = len(cost)
            
        return min(climb(n-1), climb(n-2))

"""
Recurrence Relation: Minimum Cost(i) = cost[i] + min( climb(i-1), climb(i-2) )

Time Complexity: O(2**N)
Space Complexity: O(N)  
"""

# Method 2: Memorization Top-Down DP

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(step):
            
            if step < 0:
                return 0
            if step == 0 or step == 1:
                return cost[step]
            
            if dp[step] != -1:
                return dp[step]
            
            dp[step] = cost[step] + min(climb(step-1), climb(step-2))
            return dp[step]
        
        n = len(cost)
        dp = [-1]*len(cost)
        return min(climb(n-1), climb(n-2))
    
"""
Recurrence Relation: Minimum Cost(i) = cost[i] + min( climb(i-1), climb(i-2) )

Time Complexity: O(N)
Space Complexity: O(N) + O(N) extra space for memorization  
"""

# Method 3: Bottom-Top DP

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0]*len(cost)
        
        for step in range(n):
    
            if step == 0 or step == 1:
                dp[step] = cost[step]
            else:
                dp[step] = cost[step] + min(dp[step-1], dp[step-2])
            
        
        return min(dp[n-1], dp[n-2])

"""
'NO' Recursion stack used

Time Complexity: O(N)
Space Complexity: O(N) extra space for memorization  
"""

# Method 4: Bottom-Top DP (Optimized)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        first = cost[0]
        second = cost[1]
        
        if n <=2:
            return min(first, second)
        
        for step in range(2, n):
    
                curr = cost[step] + min(first, second)
                first = second
                second = curr
        
        return min(first, second)
    
"""
Time Complexity: O(N)
Space Complexity: O(1)
"""