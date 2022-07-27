# link: https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # Two colors : A ~ 1, B ~ 2
        color = {}
        
        def dfs(node):
            
            # traversing the adjacency list of node and performing dfs recurison
            for nextNode in graph[node]:
                # if adjustend nextNode has same color then it is not bipartite
                if nextNode in color:
                    if color[nextNode] == color[node]:
                        return False
                # if not in color, we assign it opposite color
                else:
                    color[nextNode] = 1 - color[node]
                    # run dfs on it to check if it satify the condition
                    if not dfs(nextNode):
                        return False
            return True
        
        
        # traversing given graph
        for node in range(len(graph)):
            # if node not in color
            if node not in color:
                # color it as 1
                color[node] = 0
                # run dfs to check if it satisfy the condition for bipartite
                # if dfs shows False result that means not bipartite
                if not dfs(node):
                    return False
        return True

"""
Time Complexity = O(V+E) as we are visiting each cell of matrix constant number of times
Space Complexity = O(V) in worst case recursion can touch all cells of matrix
"""