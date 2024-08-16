import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().split()))
# print(numbers)
# count = 0
# def bubble_sort_times(n,arr):
#     global count
#     for i in range(n):
#         check = False
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 count += 1
#                 check = True
#         if check == False:
#             break
# bubble_sort_times(N,numbers)
# print(count)
# 버블정렬을 진짜로 구현하니깐 N^2이 되서 시간초과남

# 병합정렬을 써서 횟수를 세면 된다는데 왜 병합정렬하고 버블정렬이 같은지 모르겠음

