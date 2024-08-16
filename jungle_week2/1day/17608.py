import sys

N = int(sys.stdin.readline().strip())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
n = data[-1]
cnt = 1
while len(data) > 0 :
    if data[-1] > n:
        n = data[-1]
        cnt += 1
        del data[-1]
    else:
        del data[-1]
print(cnt)