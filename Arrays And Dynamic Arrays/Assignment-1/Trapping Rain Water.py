# Problem: https://leetcode.com/problems/trapping-rain-water/

"""
class Solution:
    def trap(self, height: List[int]) -> int:
"""
height = [int(i) for i in input().split()]

n = len(height)

Pmax = [-10**9] * n

Pmax[0] = height[0]

for i in range(1, n):
    Pmax[i] = max(Pmax[i-1], height[i])

Smax = [-10**9] * n

Smax[n-1] = height[n-1]

for i in range(n-2, -1, -1):
    Smax[i] = max(Smax[i+1], height[i])

print(Pmax)
print(Smax)

water = 0

for i in range(1, n-1):
    deciding_height = min(Pmax[i-1], Smax[i+1])
    if height[i] < deciding_height:
        water += deciding_height - height[i]

print(water)