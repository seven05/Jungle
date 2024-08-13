import sys

N = int(sys.stdin.readline().strip())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort()
# print(data)

