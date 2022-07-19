# link: https://practice.geeksforgeeks.org/problems/knight-walk4521/1

from collections import deque

def isValid(self, x, y, N):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

def minStepToReachTarget(self, KnightPos, TargetPos, N):
    #Code here
    kxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    """
    Note from the Question:
    The initial and the target position co-ordinates of Knight 
    have been given accoring to 1-base indexing.
    """
    KnightPos[0] -= 1
    KnightPos[1] -= 1
    TargetPos[0] -= 1
    TargetPos[1] -= 1
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    
    queue.append([KnightPos[0], KnightPos[1], 0])
    visited[KnightPos[0]][KnightPos[1]] = True
    
    while len(queue):
        cell = queue.popleft()
        X, Y = cell[0], cell[1]
        steps = cell[2]
        if X == TargetPos[0] and Y == TargetPos[1]:
            return steps
            
        for i in range(8):
            
            x = X + kxy[i][0]
            y = Y + kxy[i][1]
            
            if self.isValid(x, y, N) and visited[x][y] == False:
                queue.append([x, y, steps+1])
                visited[x][y] = True
                
    return -1

"""
Time Complexity = O(n*n) as we are visiting each element constant times
Space Complexity = O(n*n) 
""" 