# 알고보니 문제에 15746으로 나눈 나머지를 계산하라했는데 안넣어서 터진거였음
import sys
N = int(sys.stdin.readline().strip())
memo = [0]*((10**6)+1)
def tile(n):
    global memo
    memo[0]= 0
    memo[1]= 1
    memo[2]= 2
    if n > 2:
        for i in range(3,n+1):
            memo[i]=(memo[i-1]+memo[i-2])%15746
    return memo[n]
print(tile(N))

# 메모리초과
# import sys
# N = int(sys.stdin.readline().strip())
# memo = [0]*((10**6)+1)
# def tile(n):
#     global memo
#     memo[0]= 0
#     memo[1]= 1
#     memo[2]= 2
#     if n > 2:
#         for i in range(3,n+1):
#             memo[i]=memo[i-1]+memo[i-2]
#     return memo[n]
# print(tile(N))

# 시간초과
# import sys
# N = int(sys.stdin.readline().strip())
# stack = []
# def tile(n):
#     if n <= 2:
#         return n
#     stack.append(1)
#     stack.append(2)
#     for _ in range(3,n+1):
#         y = stack.pop()
#         x = stack.pop()
#         # print(x,y)
#         stack.append(y)
#         stack.append(x+y)
#         # print(stack)
#     return stack.pop()
# print(tile(N))