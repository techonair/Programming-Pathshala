# link: https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/

n, e = map(int, input().split())

def dfs(node, adj, visited):
    if visited[node] == 1:
        return
    visited[node] = 1
    for n in adj[node]:
        dfs(n, adj, visited)
    

adj = [[] for _ in range(n+1)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
#print(adj)

visited = [0]*(n+1)
visited[0] = 1
cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i, adj, visited)

print(cnt)

"""
Time Complexity = O(V + E) as we are visiting each node and edge only constant times
Space Complexity = O(V) as in worst case we will be store all vertices in stack
"""