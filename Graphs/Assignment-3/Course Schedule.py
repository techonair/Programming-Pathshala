# link: https://leetcode.com/problems/course-schedule-ii/

# BFS Topological Sort
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Graph = defaultdict(list)
        indegree = [0]*numCourses # shows dependencies
        
        for course, pre in prerequisites:
            Graph[pre].append(course)
            indegree[course] += 1
            
        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        topologicalOrder = []
        
        while len(queue):
            node = queue.popleft()
            
            topologicalOrder.append(node)
            
            for nextCourse in Graph[node]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        return topologicalOrder if len(topologicalOrder) == numCourses else []

"""
Time Complexity = O(N + E), where N is the number of courses and E is the number of edges, i.e, len(prerequisites). We require O(E) to form adjacency list and O(N + E) for standard BFS traversal.

Space Complexity = O(N + E), required for queue and storing prerequisites as adjacency list graph in Graph.
"""

#########################
# DFS Topological Sort #
#######################

class Solution:
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.Graph = defaultdict(list)
        self.indegree = [0]*numCourses # shows dependencies
        self.topologicalOrder = []
        
        for course, pre in prerequisites:
            self.Graph[pre].append(course)
            self.indegree[course] += 1
            
        for course in range(numCourses):
            if self.indegree[course] == 0:
                self.dfs(course)
        
        return self.topologicalOrder if len(self.topologicalOrder) == numCourses else []
                
    def dfs(self, currCourse):
        self.topologicalOrder.append(currCourse)
        self.indegree[currCourse] -= 1
        for nextCourse in self.Graph[currCourse]:
            self.indegree[nextCourse] -= 1
            if self.indegree[nextCourse] == 0:
                self.dfs(nextCourse)
                
"""                 
Time Complexity = O(N + E), We require O(E) to form adjacency list and O(N + E) for standard DFS traversal.

Space Complexity = O(N + E), required for recursive stack and storing prerequisites as adjacency list graph in G
"""