import sys
sys.stdin = open("week28/16197/16197.txt")
# o: 동전
# .: 빈 칸
# #: 벽

N, M = map(int, input().split())

board = [list(map(str, input()))for _ in range(N)]
coin = list()
for i in range(N):
    for j in range(M):
        if board[i][j] == "o":
            coin.append((i, j))
        else:
            continue    
# print(coin[0])
coin1 = coin[0]
coin2 = coin[1]

def dfs(coin1, coin2, count):

    if count > 10: # 10번이상 넘어간 경우
        return -1
    
    a, b = coin1
    c, d = coin2
    
    # 동전이 둘 다 보드 안에 있는지 확인
    if not (0 <= a < N and 0 <= b < M) and not (0 <= c < N and 0 <= d < M):
        return -1  # 둘 다 떨어진 경우
    
    # 동전 하나만 떨어진 경우, count 반환
    if not (0 <= a < N and 0 <= b < M) or not (0 <= c < N and 0 <= d < M):
        return count

    delta = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    min_count = float('inf')

    for i, j in delta:
        new_a, new_b = a + i, b + j
        new_c, new_d = c + i, d + j
        
        if 0 <= new_a < N and 0 <= new_b < M and board[new_a][new_b] == '#':
            new_a, new_b = a, b
        if 0 <= new_c < N and 0 <= new_d < M and board[new_c][new_d] == '#':
            new_c, new_d = c, d
        
        result = dfs((new_a, new_b), (new_c, new_d), count + 1)
        if result != -1: # 예외의 경우로 종료된 경우가 아니라면
            min_count = min(min_count, result) # 최소값을 갱신한다. 리턴된 카운트 값으로(하나만 떨어졌을 때의 카운트 값)

    return min_count if min_count != float('inf') else -1
    # min 카운트가 inf가 아닐경우에 min 카운트를 반환하고 아니면 -1을 반환


result = dfs(coin1, coin2, 0)
print(result)

    

        
