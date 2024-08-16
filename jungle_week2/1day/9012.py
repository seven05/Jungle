import sys

T = int(sys.stdin.readline().strip())
data = []
for i in range(T):
    data.append(list(sys.stdin.readline().strip()))
# print(data)

def push(stack):
    stack.append("(")

def pop(stack):
    if len(stack) == 0:
        return False
    if stack[-1] == "(":
        del stack[-1]
        return True
    else:
        return False

for i in data:
    # print(i)
    if i[0] != "(":
        print("NO")
        continue
    elif i[-1] != ")":
        print("NO")
        continue
    else:
        stack =[]
        chk = True
        for j in i:
            # print(j)
            if j == "(":
                push(stack)
            else:
                if pop(stack):
                    continue
                else:
                    chk = False
                    break
        # print(stack)
        if len(stack) == 0 and chk ==True:
            print("YES")
        else:
            print("NO")