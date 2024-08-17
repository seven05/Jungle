import sys

N = int(sys.stdin.readline().strip())

deck = list(i for i in range(1,N+1))
start = 0
while len(deck)-start > 1:
    start += 1                  # pop
    deck.append(deck[start])    # 맨뒤로
    start += 1                  # pop
print(deck[start])

#  ---------------
#  이렇게 하면 pop이 O(N)이기 때문에 시간 초과로 터짐
# while len(deck) > 1:
#     deck.pop(0)
#     deck.append(deck.pop(0))
# print(deck[0])
#------------------직접 큐를 생각해서 해봤는데 인덱스가 꼬임
# start = 0
# end = N-1

# while start != end :
#     deck[start] = 0
#     start = (start+2) % N
#     end = (end+2)%N
#     while deck[start] == 0:
#         start += 1
#         start = start%N
#     while deck[end] == 0:
#         end += 1
#         end = end%N
# print(deck)