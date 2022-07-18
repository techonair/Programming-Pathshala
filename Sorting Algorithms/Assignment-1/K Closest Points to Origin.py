# link: https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x):
            
            return x[0]**2 + x[1]**2
        
        points.sort(key=distance)
        #points.sort(key=lambda x: x[0]**2 + x[1]**2)
        ans = points[:k]
        
        return ans