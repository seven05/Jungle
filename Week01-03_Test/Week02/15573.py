# 시간 부족으로 미완성 ㅠㅠ
import sys
from collections import deque
N,M,K = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0 for _ in range(M)] for _ in range(N)]
que = deque()
def mining(data,d):
    cnt = 0
    for i in range(M):
        if data[0][i] <= d :
            que.append((0,i))
            visited[0][i] = 1
            cnt += 1
    for j in range(1,N):
        if data[j][0] <= d:
            que.append((j,0))
            visited[j][0] = 1
            cnt += 1
        if data[j][M-1] <= d:
            que.append((i,M-1))
            visited[i][M-1] = 1
            cnt += 1
    while que:
        row ,col = que.popleft()
        for k in range(4):
            now_r,now_c = row+dr[k],col+dc[k]
            if 0 <= now_r <=N-1 and 0 <= now_c <= M-1 :
                if visited[now_r][now_c] == 0 and data[now_r][now_c] <=d:
                    cnt += 1
                    que.append((now_r,now_c))
    if K <= cnt :
        return True
    else:
        return False
# 이분 탐색 쓰면될거같은데 시간이 모자르다    
def binary_s(s,e):
    s,e = 0,max(data)

# 다 돌면 당연히 안됨
# for i in range(1,1000000):
#     if mining(data,i):
#         print(i)

