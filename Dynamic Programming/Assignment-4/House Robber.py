# link: https://leetcode.com/problems/house-robber/

# Method 1: Brute Force - Rob current house or don't rob

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(i):
            
            if i < 0:
                return 0
            
            return max(rob(i-1), nums[i]+rob(i-2))
            
        n = len(nums)-1
            
        return max(rob(n-1), nums[n]+rob(n-2))

"""
Recurrence Relation: rob(i) = min( rob(i-1), nums[i] + rob(i-2) )

Time Complexity: O(2**N) For every house we have two condition rob it or not 
Space Complexity: O(N)  Recursion stack
"""

# Method 2: Top-Down DP with Memorization

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(i):
            
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(nums[i]+rob(i-2), rob(i-1))
            
            return dp[i]
            
        n = len(nums)-1
        dp = [-1]*(len(nums))
        
        return rob(n)

"""
Recurrence Relation: rob(i) = min( rob(i-1), nums[i] + rob(i-2) )

Time Complexity: O(N) For every house we have two condition rob it or not 
Space Complexity: O(N) + O(N) Extra Space   
"""

# Method 3: Iterative Top-Down DP with Memorization

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0]*(len(nums))
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
                
        print(dp)
        return dp[n-1]

"""
Time Complexity: O(N) For every house we have two condition rob it or not 
Space Complexity: O(N) Extra Memo Space   
"""

# Method 3: Iterative Bottom-Top DP (Optimized)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])
        
        for i in range(2, n):
            
            curr = max(first+nums[i], second)
            first = second
            second = curr
                
        return max(first, second)

"""
Time Complexity: O(N) For every house we have two condition rob it or not 
Space Complexity: O(1) 
"""   