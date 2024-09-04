# 다 못푼 코드입니다!!!

import sys
import heapq
N = int(sys.stdin.readline().strip())
lecture = []
answer = [0] * (N+1)
for _ in range(N):
    lecture.append(list(map(int,sys.stdin.readline().split())))
lecture.sort(key=lambda x:(x[1],x[2]))
# print(lecture)
heap=[]
room_cnt = 1
heapq.heappush(heap,(lecture[0][2],room_cnt))
# print(lecture[0][0])
answer[lecture[0][0]] = room_cnt
for i in range(1,N):
    # 끝시간 < 시작시간
    if heap[0][0] > lecture[i][1]:
        room_cnt += 1
        answer[lecture[i][0]] = room_cnt
        heapq.heappush(heap,(lecture[i][2],room_cnt))
    else:
        temp = heapq.heappop(heap)
        answer[lecture[i][0]] = temp[1]
        heapq.heappush(heap,(lecture[i][2],room_cnt))
print(room_cnt)
for i in range(1,len(answer)):
    print(answer[i])