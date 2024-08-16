import sys

N = int(sys.stdin.readline().strip())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
def second_big(arr):
    n = len(arr)
    if n == 1:
        return arr[0][0]
    n = n //2
    new_arr = [[0] * n for _ in range(n)]
    # print(new_arr)
    for i in range(n):
        for j in range(n):
            tmp_arr = [arr[2*i][2*j],arr[2*i][2*j+1],
                       arr[2*i+1][2*j],arr[2*i+1][2*j+1]]
            tmp_arr.sort()
            # print(tmp_arr)
            new_arr[i][j] = tmp_arr[2]
    # print(new_arr)
    return second_big(new_arr)
print(second_big(data))