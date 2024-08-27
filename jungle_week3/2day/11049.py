# 복습용
# https://e-juhee.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-11049-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-DP 
import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for term in range(1, N):
    for start in range(N):  # 첫행렬 : i, 끝행렬: i+term
        if start + term == N:  # 범위를 벗어나면 무시
            break

        dp[start][start+term] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬

        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term],
                                        # 👇 1 + 2 + 3
                                        dp[start][t]+dp[t+1][start+term] + arr[start][0] * arr[t][1] * arr[start+term][1])

print(dp[0][N-1])