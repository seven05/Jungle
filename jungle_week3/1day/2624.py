import sys

T = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
coins = []
for _ in range(K):
    coins.append(list(map(int,sys.stdin.readline().split())))
# print(coins)
dp = [0]*10001
dp[0]=0
for coin in coins:
    val, cnt = coin[0] , coin[1]
    for i in range(val,T+1):
        for j in range(1,cnt):
            dp[i] += (dp[i-val*j]+j)
print(dp[T])