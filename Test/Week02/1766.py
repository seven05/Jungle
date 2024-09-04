#  얘는 못풀었어요
import sys, heapq

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
# print(graph)
