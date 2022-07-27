# link: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(node):
            
            board[node[0]][node[1]] = "S"
            for nxt in [(1,0), (0,1), (-1,0), (0,-1)]:
                nextNode = (node[0]+nxt[0], node[1]+nxt[1])
                if 0 <= nextNode[0] < row and 0 <= nextNode[1] < col and board[nextNode[0]][nextNode[1]] == "O":
                    dfs(nextNode)
        
        row = len(board)
        col = len(board[0])
        
        "S : Safe"
        
        for i in range(row):
            for j in (0, col-1):
                if board[i][j] == "O":
                    dfs((i, j))
        
        for j in range(1, col-1):
            for i in (0, row-1):
                if board[i][j] == "O":
                    dfs((i, j))
                    
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

"""
Time Complexity = O(n*m) as we are visiting each cell of matrix constant number of time
Space Complexity = O(n*m) in worst case recursion can touch all cells of matrix
"""