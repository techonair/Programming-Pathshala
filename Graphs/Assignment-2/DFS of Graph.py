# link: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    def dfsOfGraph(self, V, adj):
            # code here
            visited = [0]*V
            df = []
            self.dfs(0, adj, visited, df)
            return df
            
    def dfs(self, node, adj, visited, df):
        if visited[node] == 1:
            return
        visited[node] = 1
        df.append(node)
        for n in adj[node]:
            self.dfs(n, adj, visited, df)

"""
Time Complexity = O(V + E) as we are visiting each node and edge only constant times
Space Complexity = O(V) as in worst case we will be store all vertices in stack
"""