# 검색해서 찾아봄 복습필요
import sys

N = int(sys.stdin.readline().strip())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(cost)
dp = [[float('inf')]* (1 << N) for _ in range(N)]

def dfs(x, visited):
    if visited == (1 << N) - 1:     # 모든 도시를 방문했다면
        if cost[x][0]:             # 출발점으로 가는 경로가 있을 때
            return cost[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return float('inf')

    if dp[x][visited] != float('inf'):       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, N):           # 모든 도시를 탐방
        if not cost[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue
        # 점화식 부분 
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + cost[x][i])
    return dp[x][visited]
print(dfs(0, 1))