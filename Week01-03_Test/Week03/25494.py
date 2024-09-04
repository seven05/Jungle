import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    result = 0
    data = list(map(int,sys.stdin.readline().split()))
    for i in range(1,data[0]+1):
        for j in range(1,data[1]+1):
            for k in range(1,data[2]+1):
                if i % j == j % k and j % k == k % i :
                    result += 1
    print(result)
