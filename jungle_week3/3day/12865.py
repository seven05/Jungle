# 1차원 dp 테이블을 사용하는경우
import sys
N,K = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
dp = [0]*(K+1)
for i in data:
    W,V = i[0],i[1]
    for w in range(K,W-1,-1):
        dp[w]=max(dp[w],dp[w-W]+V)
print(dp[K])

# 2차원 dp테이블을 사용하는경우
# for i in range(1, N + 1):
#     weight, value = items[i - 1]
#     for w in range(K + 1):
#         if w < weight:
#             # 현재 물건을 담을 수 없는 경우, 이전 상태를 그대로 가져옵니다.
#             dp[i][w] = dp[i - 1][w]
#         else:
#             # 물건을 담지 않는 경우 vs 물건을 담는 경우 중 최대 가치를 선택
#             dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)