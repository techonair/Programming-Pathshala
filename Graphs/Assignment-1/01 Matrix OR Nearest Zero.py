# link: https://leetcode.com/problems/01-matrix/submissions/

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        deque = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    deque.append((i, j))
                    
        while deque:
            x, y = deque.pop(0)
            
            for search in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextX, nextY = x + search[0], y + search[1]
                
                if 0 <= nextX < m and 0 <= nextY < n and (nextX, nextY) not in visited:
                    matrix[nextX][nextY] = matrix[x][y] + 1
                    visited.add((nextX, nextY))
                    deque.append((nextX, nextY))
                    
        return matrix

"""
Time Complexity = O(3(m*n)) ~ O(m*n) as we are visiting each element constant times
Space Complexity = O(m*n) as in worst case we will be storing all indices of matrix 
""" 