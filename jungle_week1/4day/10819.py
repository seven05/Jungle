import sys
from itertools import permutations
N= int(sys.stdin.readline().strip())
# print(N)
data = list(map(int, sys.stdin.readline().split()))
# print(data)
def cal(arr):
    result = 0
    for i in range(1,len(arr)):
        result += (abs(arr[i-1]-arr[i]))
    return result
all_array = list(permutations(data))
# print(all_array)
cal_max = 0
for array in all_array:
    cal_max = max(cal(array),cal_max)
print(cal_max)

# ----------최대-최소-최대-최소(답아님) ---------------
# for i in range(N):
#     if(i % 2 == 0):
#         pick.append(data[N-1-(i//2)])
#     else:
#         pick.append(data[i//2])
# -------------------------------------------
# --------순열 구현하려다가 버그 해결 못함 -----
# def permuta(arr,r):
#     used = [0 for _ in range(len(arr))]
#     def permu(chosen,used):
#         if len(chosen) == r:
#             calchose_val = cal(chosen)
#             if (calchose_val > cal_max):
#                 cal_max = calchose_val
#             return 
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 permu(chosen,used)
#                 used[i] = 0
#                 chosen.pop()
#     permu([],used)
# permuta(data,N)
# print(cal_max)
# -------------------------------------------