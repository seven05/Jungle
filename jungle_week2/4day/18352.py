import sys
from collections import deque
N,M,K,X = map(int,sys.stdin.readline().split())
# print(N,M,K,X)
graph = {i: [] for i in range(1, N + 1)}
# print(graph) {1: [], 2: [], 3: [], 4: []}
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b) 
# print(graph) {1: [2, 3], 2: [3, 4], 3: [], 4: []}

def bfs(n,k,x,graph):
    d = [-1]*(n+1)
    d[x] = 0
    que = deque([x])
    while que:
        cur_city = que.popleft()
        for next_city in graph[cur_city]:
            if d[next_city] == -1:
                d[next_city] = d[cur_city]+1
                que.append(next_city)
    result = []
    for i in range(1,n+1):
        if d[i] == k:
            result.append(i)
    return result

answer = bfs(N,K,X,graph)
answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)
