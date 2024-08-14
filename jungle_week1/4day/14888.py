import sys
# from itertools import permutations
# 중복제거 + 리스트에 담지않는 최적화 생각해보기

n= int(sys.stdin.readline().strip())
nums = (list(map(int, sys.stdin.readline().split())))
add, sub, mul, div = map(int,sys.stdin.readline().split())
# print(add,sub,mul,div)
def dfs(i, res, add, sub, mul, div):
    global max_val, min_val
    if i == n:
        max_val = max(max_val, res)
        min_val = min(min_val, res)
        return
    if add:
        dfs(i + 1, res + nums[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, res - nums[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, res * nums[i], add, sub, mul - 1, div)
    if div:
        if res < 0:
            dfs(i + 1, -(-res // nums[i]), add, sub, mul, div - 1)
        else:
            dfs(i + 1, res // nums[i], add, sub, mul, div - 1)

max_val = -1000000000
min_val = 1000000000

dfs(1, nums[0], add, sub, mul, div)

print(max_val)
print(min_val)

# symbols =[]
# for i in range(4):
#     for j in range(symbol[i]):
#         symbols.append(i)
       
# # print(symbols)
# # all_num_arrays = list(permutations(num))
# all_symbols_arrays = list(permutations(symbols))
# # print(all_num_arrays)
# # print(all_symbols_arrays)
# def cal(n1,n2,s):
#     if s == 0:
#         return  n1 + n2
#     elif s == 1:
#         return  n1 - n2
#     elif s == 2:
#         return  n1 * n2
#     else:
#         if n1 < 0 :
#             return (-(abs(n1)//n2))
#         else:
#             return n1 // n2
# result_max=-1000000000
# result_min=1000000000
# for i in all_symbols_arrays:
#     for j in range(N):
#         temp = num[0]
#         if N == 2:
#            result_max,result_min =cal(num[j],num[j+1],i[0])
#         else:
#             for k in range(N-1):
#                 temp = cal(temp,num[k+1],i[k])
#             result_max = (max(result_max,temp))
#             result_min = (min(result_min,temp))
# print(result_max)
# print(result_min)

