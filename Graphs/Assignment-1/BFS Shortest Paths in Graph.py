# link: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from collections import defaultdict, deque
t = int(input())

class Graph:
    
    # constructor to declare node and adjacency list
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(lambda: [])
        
    def connect(self, x, y):
        """
        We are connecting two nodes with each other by 
        appending y in adjacency list of x and x in adjacency list of x
        """
        self.adj[x].append(y)
        self.adj[y].append(x)
        
    def find_all_distances(self, root):
        distance = [-1]*self.n
        visited = [False]*self.n
        
        q = deque()
        q.append(root)
        distance[root] = 0
        visited[root] = True
        
        while len(q) != 0:
            node = q.pop()
            neighbours = self.adj[node]
            height = distance[node]
            
            for neighbour in neighbours:
                if visited[neighbour] == False: 
                    distance[neighbour] = height + 6
                    visited[neighbour] = True
                    q.appendleft(neighbour)
        
        distance.pop(root)
        print(" ".join(map(str, distance)))

for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)

"""
Time Complexity = O(V*E) as we are visiting each node and edge only constant times
Space Complexity = O(V*E) as in worst case we will be store all vertices and edges 
""" 