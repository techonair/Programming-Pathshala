# link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    
    def dfsCycleFound(self, node, visited):
        if visited[node]:
            if visited[node] == 1:
                return True
            return
        
        visited[node] = 1
        for nextNode in adj[node]:
            if self.dfsCycleFound(nextNode, visited):
                return True
        visited[node] = 2
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        visited = [0 for _ in range(V)]
        
        for node in range(V):
            if not visited[node]:
                if self.dfsCycleFound(node, visited):
                    return True
        return False

"""
Time Complexity = O(V+E) as we are visiting each node constant number of time
Space Complexity = O(V) in worst case recursion can store all nodes
"""