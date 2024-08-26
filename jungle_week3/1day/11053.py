import sys

N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
# print(data)
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
 
print(max(dp))