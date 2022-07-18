# Link: https://www.codechef.com/problems/MM1803

def PossiblePaths(grid, i, j, rat):
    if i < 0 or j < 0 or i == n or j == n or grid[i][j] == 0:
        return
    if i == j and j == n-1:
        path.append(rat.copy())
        #rat.clear()
        return

    grid[i][j] = 0
    rat.append('D')
    PossiblePaths(grid, i+1, j, rat)
    if len(rat): rat.pop()
    rat.append('L')
    PossiblePaths(grid, i, j-1, rat)
    if len(rat): rat.pop()
    rat.append('U')
    PossiblePaths(grid, i-1, j, rat)
    if len(rat): rat.pop()
    rat.append('R')
    PossiblePaths(grid, i, j+1, rat)
    if len(rat): rat.pop()
    grid[i][j] = 1

for _ in range(input()):
    n = int(input())
    m = list(map(int,input().split()))
    grid = [[0 for i in range(n)] for j in range(n)]
    k=0
    for i in range(n):
        for j in range(n):
            grid[i][j] = m[k]
            k+=1
    path = []
    rat = []
    PossiblePaths(grid, 0, 0, rat)
    for i in range(len(path)):
        print("".join(path[i]), end=" ")
    print('\n', end="")
        