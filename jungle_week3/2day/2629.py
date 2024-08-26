import sys 

int(sys.stdin.readline().strip())
chu = list(map(int,sys.stdin.readline().split()))
# print(chu)
can_make = set()
for cur in chu:
    next_make = {cur}
    for temp in can_make:
        next_make.add(abs(temp - cur))
        next_make.add(temp + cur)
    can_make |= next_make

int(input())
c = list(map(int,sys.stdin.readline().split()))
if c in can_make:
    print('Y')
else:
    print('N')
