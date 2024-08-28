#가장긴 부분수열 시간복잡도 더 낮은 버전
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

LIS = [nums[0]]

for num in nums:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        start = 0
        end = len(LIS)-1        
        while start <= end:
            mid = (start+end)//2
            
            if LIS[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        
        LIS[start] = num
        
print(len(LIS))
#https://eatchangmyeong.github.io/2022/01/20/why-is-lis-algorithm-so-confusing.html
# LIS 알고리즘 보면 좋은 참고자료