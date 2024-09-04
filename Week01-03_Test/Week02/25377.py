import sys

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
time = 1001
for i in data:
    if i[0] > i[1]:
        temp_time = 1001
    else:
        temp_time = i[1]
    time = min(temp_time,time)
if time == 1001:
    print(-1)
else:
    print(time)