# link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def isValid(NextNode):
            return 0 <= NextNode[0] < m and 0 <= NextNode[1] < n 
        
        def dfs(node):
            if grid[node[0]][node[1]] == "0":
                return
            if node in visited:
                return
            visited.add(node)
            for nxt in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                NextNode = (node[0] + nxt[0], node[1] + nxt[1])
                if isValid(NextNode) and NextNode not in visited:
                    dfs(NextNode)
        
        m = len(grid)
        n = len(grid[0])
        
        ones = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ones.append((i,j))
        
        visited = set()
        NumberOfIslands = 0
        
        for coordinate in ones:
            if coordinate not in visited:
                NumberOfIslands += 1
                dfs(coordinate)
        
        return NumberOfIslands
                
"""
Time Complexity = O(V * E) ~ O(n*m)
                        
                            V = n * m
                            E = ((n*m)*4)/2 = 2(n*m)
                            Time Complexity =  O(nm + 2nm) = O(3nm) ~ O(n*m)

Space Complexity = 0(n*m)

                visited + recursion stack ~ O(n*m) as in worst case we will be store all cells of grid in stack
"""