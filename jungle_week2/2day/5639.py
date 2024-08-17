import sys
sys.setrecursionlimit(1000000)
preorder = []
# count = 0 이렇게 하니깐 헷갈림
while True:
    try:
        preorder.append(int(sys.stdin.readline().strip()))
        # count += 1
    except:
        break
# print(count)
print(preorder)
def postorder(s,e):
    if s > e:
        return 
    mid = e + 1
    for i in range(s+1,e+1):
        if preorder[s] < preorder[i] :
            mid = i
            break
    postorder(s+1,mid-1)
    postorder(mid,e)
    print(preorder[s])

postorder(0,len(preorder)-1)