# 외판원 순회 DFS 버전 복습용

n = int(input()) # 도시의 수
cost = [list(map(int, input().split())) for _ in range(n)] # 도시 간 이동 비용

visit = [0]*n # 0, 1, 2 ... n-1 인덱스에 n개의 도시 방문 여부 기록
answer = 1000000*10 # 나올 수 있는 최대 정답 (최대 비용*최대 도시)

def dfs(start, now, costsum):
    global answer # 함수 밖의 answer 활용한 조건문 존재하므로
    
    if costsum > answer:
        return # 이미 answer 보다 비용이 높다면, 이후 경로들을 고민할 필요가 없음
    
    if start == now and 0 not in visit: # 모든 도시를 순환형으로 방문했다면
        if costsum < answer:
            answer = costsum # costsum이 answer보다 작을 경우 갱신
        return # 갱신 여부와 상관없이 재귀로 들어간 함수에서 나오기 위한 장치
    
    for i in range(n): # 다음 목적지 i
        if cost[now][i] != 0 and visit[i] == 0: # 갈 수 있으며 아직 안 가 봤다면
            visit[i] = 1
            dfs(start, i, costsum+cost[now][i])
            visit[i] = 0 # 방문 해제
            		# costsum은 함수에서 직접 더해주므로 재귀로 들어간 함수에서 나오면 초기화
                        # 하지만 visit 리스트는 이와 상관없으므로 직접 방문 해제 처리해야 함
            
dfs(0, 0, 0) # 순환형이므로 어디부터 탐색하던 상관이 없음. 따라서 0번 인덱스에서 시작하는 것으로 지정
print(answer)