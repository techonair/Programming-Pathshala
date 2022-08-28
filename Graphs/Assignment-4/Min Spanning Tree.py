# link: https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

# Kruskal Algorithm: sorted edges -> iterate edges -> check no cycle, find()/getRoot() -> union()

class Solution:
    
    def __init__(self):
        self.root = []
        self.size = []
        self.edges = []
        
    def makeset(self, v):
        self.root[v] = v
        self.size[v] = 0

    """ * Main Function * """
    def spanningTree(self, V, adj):
        
        cost = 0
        self.root = [0]*V
        self.size = [0]*V
        
        # step 0: initialize the root and size
        for i in range(V):
            self.makeset(i)
            
        #print(root)
        #print(size)
        
        # step 1: create the list of edges and sort them
        self.createEdgeList()
        #print(edges)
        
        # step 2: iterate EdgeList and check if they are already part of MST or not if True skip else union
        # as we are considering minimum cost edges first so cost will automatically be minimum 
        for edge in self.edges:
            if self.getRoot(edge[1]) != self.getRoot(edge[2]):
                # step 3: add up the cost of this edge and perform union(edge1, edge2)
                cost += edge[0]
                self.union(edge[1], edge[2])
                
        return cost
        
    # creates sorted edge list (Preprocessing for Krushal Algorithm)
    def createEdgeList(self):
        
        for i in range(V):
            for j in range(len(adj[i])):
                edge = adj[i][j]
                
                tmp = []
                tmp.append(edge[1])
                tmp.append(min(i, edge[0]))
                tmp.append(max(i, edge[0]))
                
                self.edges.append(tmp)
        #print(edges)
        self.edges.sort(key = lambda x:x[0])
        #print(self.edges)
    
    def getRoot(self, v):
        # finds root of a vertice
        while self.root[v] != v:
            v = self.root[v]
        return v
        """
        if v == self.root[v]:
            return v
        self.root[v] = self.getRoot(self.root[v])
        return self.root[v]
        """
        
    def union(self, edge1, edge2):
        root1 = self.getRoot(edge1)
        root2 = self.getRoot(edge2)
        size1 = self.size[root1]
        size2 = self.size[root2]
        
        # attaching to bigger connected component
        if size1 > size2:
            self.root[root2] = root1
            self.size[root1] += size2
            
        else:
            # attaching to smaller or same size component/ Multiple MSTs can be there
            self.root[root1] = root2
            self.size[root2] += size1
            
"""
Time Complexity = O(V * E) ~ O(n*m)
                        
->  Precomputation:                 Sorting edges = ElogE

->  Iterating on E edges:           E      {max. edges can be V^2}
    find()/getRoot() and union():   logV   {as we have a tree to search and union}
                                
    Final Time Complexity =  O(ElogE + ElogV)

Space Complexity = 0(E + V)

                visited + recursion stack ~ O(n*m) as in worst case we will be store all cells of grid in stack
"""