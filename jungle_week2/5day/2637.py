import sys
from collections import defaultdict
N = int(sys.stdin.readline().strip())  # 부품수
M = int(sys.stdin.readline().strip())  # 부품간의 관계 
graph = defaultdict(list)
for _ in range(M):
    x, y, k = map(int,sys.stdin.readline().split())
    graph[y].append((x, k))  # y -> x (y를 만들기 위해 x가 k개 필요)
print(graph)

