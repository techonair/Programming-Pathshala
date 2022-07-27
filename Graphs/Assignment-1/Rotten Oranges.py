# link: 
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        cnt = 0
        while fresh > 0 and len(queue) > 0:
            
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for nxt in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextX = x + nxt[0] 
                    nextY = y + nxt[1]

                    if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] == 1:
                        grid[nextX][nextY] = 2
                        queue.append((nextX, nextY))
                        fresh -= 1
            cnt += 1
            
        if fresh:
            return -1
        
        return cnt
                    
"""
Time Complexity = O(m*n) each cell is visited at least once
Space Complexity = O(m*n) in the worst case if all the oranges are rotten they will be added to the queue 
""" 