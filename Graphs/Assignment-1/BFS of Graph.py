# link: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        ans = []
        q = deque()
        visited = [0]*V
        
        q.append(0)
        visited[0] = 1
        
        while len(q) != 0:
            
            n = q.pop()
            ans.append(n)
            
            for num in adj[n]:
                
                if visited[num] == 0:
                    q.appendleft(num)
                    visited[num] = 1
                    
        return ans

"""
Time Complexity = O(V + E) as we are visiting each node and edge only constant times
Space Complexity = {O(V) for vertices + O(N) for queue} ~ 'O(V)' as in worst case we will be store all vertices and edges 
"""