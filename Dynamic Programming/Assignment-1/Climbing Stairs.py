# link: https://leetcode.com/problems/climbing-stairs/

"""

Method 1) Using Optimal Structure 

Recurrence Relation: F(i) = F(i+1) + F(i+2)
Time Complexity: O(2**N)  {Binary Tree with height N}
Space Complexity: O(N)    {Recursion Call Stack}

Code:

class Solution:
    def climbStairs(self, n: int) -> int:
        
        i = 0
        def TotalWays(i):
            
            if i == n:
                return 1
            elif i > n:
                return 0
            
            ways = TotalWays(i+1) + TotalWays(i+2)
            
            return ways
        
        return TotalWays(i)
        
            
"""

"""

Method 2) Top-Bottom DP (Using Optimal Structure + Memorization Array) 

Recurrence Relation: F(i) = F(i+1) + F(i+2)
Time Complexity: O(N)  {Total calls = N and O(1) constant work}
Space Complexity: O(N)    {Memorization Array}

Code:

class Solution:
    def climbStairs(self, n: int) -> int:
        
        i = 0
        ways = [-1] *n
        def TotalWays(i):
            
            if i == n:
                return 1
            elif i > n:
                return 0
            
            if ways[i] != -1:
                return ways[i]
            else:
                ways[i] = TotalWays(i+1) + TotalWays(i+2)
            
            return ways[i]
        
        return TotalWays(i)
        

"""

"""
Method 3) Bottom-Top DP (Fibonacci) 

Recurrence Relation: F(i) = F(i+1) + F(i+2)
Time Complexity: O(N)  {For loop runs for N and O(1) constant work/iteration}
Space Complexity: O(1)  

Code:

class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = 1
        second = 2
        
        if n == first:
            return first
        elif n == second:
            return second
        else:
            for i in range(3, n+1):
                curr = first + second
                first = second
                second = curr
            
        return second

"""