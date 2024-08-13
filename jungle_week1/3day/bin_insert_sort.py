import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))

def binary_insertion_sort(a) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
            if a[pc] == key:     # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
    
        pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

binary_insertion_sort(data)

for i in range(N):
    print(data[i])