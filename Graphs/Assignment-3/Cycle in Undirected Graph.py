# link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:

    #Function to detect cycle in an undirected graph
	def isCycle(self, V, adj):
		#Code here
		visited = [False for _ in range(V)]
		for node in range(V):
		    if not visited[node]:
		        if self.dfsCycleFound(node, node, visited):
		            return True
		return False
    
    def dfsCycleFound(self, node, Prev, visited):
        
        if visited[node]:
            return True

        visited[node] = True
        for nextNode in adj[node]:
            if nextNode != Prev:
                if self.dfsCycleFound(nextNode, node, visited):
                    return True
        return False

"""
Time Complexity = O(V+E) as we are visiting each node constant number of time
Space Complexity = O(V) in worst case recursion can store all nodes
"""