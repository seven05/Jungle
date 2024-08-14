import sys

N,K = map(int,sys.stdin.readline().split())
Levels = []
for i in range(N):
    Levels.append(int(sys.stdin.readline().strip()))
Levels.sort()
# print(Levels)
def max_level(levels):
    low, high = min(levels), (max(levels) + K)

    while low <= high:
        mid = (low + high) // 2
        req = sum(max(0, mid - level) for level in levels)

        if req <= K:
            low = mid + 1
        else:
            high = mid - 1

    return high
print(max_level(Levels))