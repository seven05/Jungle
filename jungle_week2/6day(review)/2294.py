from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
coins = set(int(sys.stdin.readline()) for _ in range(n))
check = [0 for _ in range(k+1)]
que = deque()
for coin in coins:
    if coin > k:
        continue
    que.append([coin, 1])
    check[coin] = 1
# print(coins)
flag = True
while que:
    val, cnt = que.popleft()
    if val == k:
        print(cnt)
        flag = False
        break
        
    for coin in coins:
        if val + coin > k:
            continue
        if check[val+coin] == 0:
            check[val+coin] = 1
            que.append([val+coin, cnt+1])
            
if flag:
    print(-1)