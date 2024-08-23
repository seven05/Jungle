import sys

T = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
coins = []
for _ in range(K):
    coins.append(list(map(int,sys.stdin.readline().split())))
# print(coins)
dp = [0]*(T+1)
dp[0]=1
for val, cnt in coins:
    for i in range(T, 0, -1):  
        for j in range(1, cnt + 1):
            if i >= j * val:
                dp[i] += dp[i - j * val]
print(dp[T])