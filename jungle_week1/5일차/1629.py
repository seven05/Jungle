import sys
sys.setrecursionlimit(1000000)
A,B,C = map(int,sys.stdin.readline().split())
# print(A,B,C)

def func(a,b,c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = func(a,b//2,c)
        return (half * half) % c
    else:
        return (a * func(a,b-1,c))%c
result = func(A,B,C)
print(result)

# ---------------------------------
# 이론
# A^B % C = 
# A%C
# A^2 %C 
# ((A % C) ** B ) % C
# A mod C = r1
# A = Cx + r1
# A^2 = C^2 x^2 + 2r1Cx + r1^2
# A^2 mod C = r1^2 mod C
# ---------------------------------
# 시간 초과
# r = A%C
# for i in range(B-1):
#     r = r*r
#     r = r%C
# ---------------------------------
# 메모리 초과
# cnt=0
# def rmodulerc(r,cnt):
#     if cnt == B:
#         print(r%C)
#         return
#     r = r % C
#     cnt += 1
#     rmodulerc(r*r,cnt)
# rmodulerc(A,0)
# ---------------------------------

