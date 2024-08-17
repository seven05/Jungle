import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
apple = []
for i in range(K):
    apple.append(list(map(int,sys.stdin.readline().split())))
L = int(sys.stdin.readline().strip())
snake = []
for i in range(L):
    snake.append(list(sys.stdin.readline().split()))
# print(apple,snake)
