# Link: https://leetcode.com/problems/unique-paths-iii/

def PossiblePaths(grid, r, c, isVisited):
    if r < 0 or c < 0 or r == row or c == column or grid[r][c] == -1 or isVisited[r][c]==False: #or grid[r][c] == 1:
        return
    if grid[r][c] == 2:
        cnt = 0
        cnt += 1
        return cnt

    isVisited = False
    PossiblePaths(grid, r+1, c, isVisited)
    PossiblePaths(grid, r-1, c, isVisited)
    PossiblePaths(grid, r, c+1, isVisited)
    PossiblePaths(grid, r, c-1, isVisited)
    if grid[r][c] != 1:
        grid[r][c] = 0
    else:
        grid[r][c] = 1
    isVisited = True
    
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
row = len(grid)
column = len(grid[0])
isVisited = [[True]*column]*row

for i in range(row):
    for j in range(column):
        if grid[i][j] == 1:
            r, c = i, j
        #if grid[i][j] == 2:
        #    x, y = i, j

print(PossiblePaths(grid, r, c, isVisited))