import sys

N,M = map(int,sys.stdin.readline().split())
maze=[]
for _ in range(N):
    maze.append(list(map(int,sys.stdin.readline().strip())))
print(maze)
