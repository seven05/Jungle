import sys

N,M = map(int,sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:  # 방문하지 않은 정점이 있으면 새로운 연결 요소
        dfs(graph, i, visited)
        count += 1  # 연결 요소의 개수 증가

print(count)