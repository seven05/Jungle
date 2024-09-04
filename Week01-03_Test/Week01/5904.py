import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline().strip())
K = 0
Length = 3
while Length < N:
    K += 1
    Length = 2 * Length + (K + 3) 
# print(K)
def find_n(k,n,length):
    global prev_len
    if k == 0:
        return "moo"[n-1]   
    prev_len = (length-(k+3)) // 2
    mid_len = k + 3
    if n < prev_len:
        return find_n(k - 1, n,prev_len)
    elif n < prev_len + mid_len:
        if n == prev_len+1:
            return "m"
        else:
            return "o"
    else:
        return find_n(k - 1, n - prev_len - mid_len,prev_len)

print(find_n(K,N,Length))

# K = 0
# def moo(k):
#     if k==0:
#         return "moo"
#     return moo(k-1) + "m" + "o"*(k+2) + moo(k-1)
# for i in range(int(N ** (1/2))):
#     if len(moo(i)) > N:
#         K = i
#         break
# # print(len(moo(N)))
# # print(K)
# # print(moo(K))
# print(moo(K)[N-1])
# 직접 문자열 만들면 시간초과
# count = 0
# K=0
# def moo_cnt(n):
#     global count
#     if n==0:
#         count += 3
#         return 1
#     count += (n+3)
#     return moo_cnt(n-1) + moo_cnt(n-1)
# def moo(k):
#     if k==0:
#         return [1,2]
#     return moo(k-1) + [1,k+2] + moo(k-1)
# i=0
# while count < N :
#     count = 0
#     moo_cnt(i)
#     i += 1
# K = i
# # print(moo_cnt(N))
# result = moo(K)
# result_sum =0
# for i in range(len(result)):
#     result_sum += result[i]
#     if result_sum >= N:
#         if result[i] == 1 :
#             print("m")
#         else :
#             print("o")
#         break
#  이것도 시간초과 ㅠ