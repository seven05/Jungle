import sys
from itertools import permutations
# 중복제거 + 리스트에 담지않는 최적화 생각해보기
n= int(sys.stdin.readline().strip())
nums = (list(map(int, sys.stdin.readline().split())))
symbols_count = list(map(int, sys.stdin.readline().split()))  # 각 연산자의 개수
symbols = []
symbols += ['+'] * symbols_count[0]
symbols += ['-'] * symbols_count[1]
symbols += ['*'] * symbols_count[2]
symbols += ['//'] * symbols_count[3]

# 최댓값과 최솟값 초기화
max_value = -float('inf')
min_value = float('inf')

# 연산자의 모든 순열에 대해 계산
for perm in set(permutations(symbols, len(symbols))):
    result = nums[0]
    for i in range(n - 1):
        if perm[i] == '+':
            result += nums[i + 1]
        elif perm[i] == '-':
            result -= nums[i + 1]
        elif perm[i] == '*':
            result *= nums[i + 1]
        elif perm[i] == '//':
            if result < 0:
                result = -(-result // nums[i + 1])
            else:
                result //= nums[i + 1]
    max_value = max(max_value, result)
    min_value = min(min_value, result)
print(max_value)
print(min_value)
