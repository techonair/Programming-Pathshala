# link: https://practice.geeksforgeeks.org/problems/topological-sort/1

from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0]*V
        
        for i in range(V):
            for j in range(len(adj[i])):
                indegree[adj[i][j]] += 1
        
        queue = deque()
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        topologicalOrder = []
        
        while len(queue):
            node = queue.popleft()
            
            topologicalOrder.append(node)
            
            for j in range(len(adj[node])):
                indegree[adj[node][j]] -= 1
                if indegree[adj[node][j]] == 0:
                    queue.append(adj[node][j])
        
        return topologicalOrder

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)

"""
Time Complexity = O(V+E) as we are visiting each node constant number of time
Space Complexity = O(V) in worst case recursion can store all nodes
"""