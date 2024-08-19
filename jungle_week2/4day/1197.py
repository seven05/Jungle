import sys

V,E = map(int,sys.stdin.readline().split())
data = []
for _ in range(E):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
data.sort(key=lambda x:x[2])
# print(data)
parent = list(i for i in range(1,V+1))
# print(parent)

def find(x):        # 부모가 자기자신이 아닌경우에 재귀적으로 부모를 찾을때까지 타고올라감
    global parent
    if parent[x] != x:        
        parent[x] = find(parent[x])
    return parent[x-1]      

def union(x,y):
    pX,pY = find(x),find(y)
    if pX > pY :
        parent[pX] = pY
    else:
        parent[pY] = pX

# 미완성 rank의 필요성이나 기능을 다 몰라서 stop


