# 가장 긴 증가하는 부분수열 구하기 문제랑 같음
# 결국 수열을 이루는 애들을 빼고 전부 옮겨야 순서가 맞기 때문에
import sys

N = int(sys.stdin.readline().strip())
children = [0]
for _ in range(N):
    children.append(int(sys.stdin.readline().strip()))
dp = [1] * (N+1)
for i in range(1,N+1):
    for j in range(1,i):
        if children[i]>children[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(N - max(dp))