# link: https://leetcode.com/problems/k-closest-points-to-origin/

# Method 1: Custom Sorting
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x):
            
            return x[0]**2 + x[1]**2
        
        points.sort(key=distance)
        #points.sort(key=lambda x: x[0]**2 + x[1]**2)
        ans = points[:k]
        
        return ans

"""
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

# Method 2: Min Heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = lambda x, y: x*x + y*y
        for p in points:
            # at each subcell of points at index 0 we are inserting distance -> [distance,x,y] 
            p.insert(0, distance(p[0], p[1]))
        heapq.heapify(points)
        return [heapq.heappop(points)[1:] for _ in range(k)]

"""
Time Complexity: O(N+KlogN)
Space Complexity: O(K)
"""

# Method 2.1: Max Heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x):
            
            return x[0]**2 + x[1]**2
        
        heap = []
        
        for i, p in enumerate(points):
            
            d = distance(p)
            if len(heap) == k:
                heapq.heappushpop(heap, (-d, i))
            else:
                heapq.heappush(heap, (-d, i))
                
        return [points[i] for (_, i) in heap]

"""
Time Complexity: O(NlogK)
Space Complexity: O(K)
"""