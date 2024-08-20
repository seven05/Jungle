from collections import deque
import sys
# 입력 처리
R, C = map(int, sys.stdin.readline().split())
forest = []
water_queue = deque()
hedgehog_queue = deque()
visited = [[False] * C for _ in range(R)]

for i in range(R):
    row = list(input().strip())
    forest.append(row)
    for j in range(C):
        if row[j] == 'S':  # 고슴도치의 시작 위치
            hedgehog_queue.append((i, j, 0))
            visited[i][j] = True
        elif row[j] == '*':  # 물의 시작 위치
            water_queue.append((i, j))

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 실행
while hedgehog_queue:
    # 물이 먼저 퍼져나감
    for _ in range(len(water_queue)):
        wx, wy = water_queue.popleft()
        for i in range(4):
            nwx = wx + dx[i]
            nwy = wy + dy[i]
            if 0 <= nwx < R and 0 <= nwy < C and forest[nwx][nwy] == '.':
                forest[nwx][nwy] = '*'
                water_queue.append((nwx, nwy))

    # 고슴도치 이동
    for _ in range(len(hedgehog_queue)):
        hx, hy, time = hedgehog_queue.popleft()
        for i in range(4):
            nhx = hx + dx[i]
            nhy = hy + dy[i]
            if 0 <= nhx < R and 0 <= nhy < C:
                if forest[nhx][nhy] == 'D':  # 비버의 굴에 도착한 경우
                    print(time + 1)
                    exit()
                if forest[nhx][nhy] == '.' and not visited[nhx][nhy]:  # 이동 가능하고 방문하지 않은 곳
                    visited[nhx][nhy] = True
                    hedgehog_queue.append((nhx, nhy, time + 1))

# 비버의 굴에 도달할 수 없는 경우
print("KAKTUS")
