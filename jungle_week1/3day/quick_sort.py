import sys
N = int(sys.stdin.readline())
limit_number = 15000
sys.setrecursionlimit(limit_number)
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))

def qsort(a, left: int, right: int):
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

qsort(data,0,N-1)

for i in range(N):
    print(data[i])