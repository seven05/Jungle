import sys

N = int(sys.stdin.readline().strip())
command = []
for i in range(N):
    command.append(list(sys.stdin.readline().split()))
# print(command)
Que = []
start = 0
count = 0
def push(x):
    global count
    Que.append(x)
    count += 1

def pop():
    global start
    global count
    if count > 0:
        print(Que[start])
        start += 1
        count -= 1
    else:
        print(-1)

def size():
    global count
    print(count)

def empty():
    global count
    global start
    if count == 0:
        print(1)
    else:
        print(0)

def front():
    global start
    global count
    if count > 0:
        print(Que[start])
    else:
        print(-1)

def back():
    global count
    if count > 0:
        print(Que[-1])
    else:
        print(-1)

for i in command:
    if i[0] == "push":
        push(i[1])
    elif i[0] == "pop":
        pop()
    elif i[0] == "size":
        size()
    elif i[0] == "empty":
        empty()
    elif i[0] == "front":
        front()
    elif i[0] == "back":
        back()
