import sys
sys.stdin = open("week33/17144/17144.txt")
from collections import deque

R, C, T = map(int, input().split()) # 행 - , 열 ㅣ, 시간 

# 1. 확산이 일어난다. 칸의 숫자/5
# 2. 칸의 남은숫자 = 칸의 숫자 - 칸의 숫자/5 * 확산된 방향의 갯수
# 3. 공기 청정기 작동 벽쪽만 움직이나 본대
# 시간만큼 진행된다.
# 남은 먼자의 양 결과

room = [list(map(int, input().split())) for _ in range(R)]
clean_wind = [(i, j) for i in range(R) for j in range(C) if room[i][j] == -1]


def spread():
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while dust:
        a, b = dust.popleft()
        tmp_count = 0
        for dr, dc in delta:
            na, nb = a + dr, b + dc
            if 0 <= na < R and 0 <= nb < C and room[na][nb] != -1:
                room[na][nb] += room[a][b]/5
                tmp_count += 1
        room[a][b] = room[a][b] - room[a][b]/5 * tmp_count
        
def wind():
    
    fa, fb = clean_wind[0]
    
    # 상단 청정기 작동 - 반시계 방향으로 이동
    for x in range(fa - 1, 0, -1):  
        room[x][0] = room[x - 1][0]
    for y in range(0, C - 1):  
        room[0][y] = room[0][y + 1]
    for x in range(0, fa):  
        room[x][C - 1] = room[x + 1][C - 1]
    for y in range(C - 1, 1, -1):  
        room[fa][y] = room[fa][y - 1]
    room[fa][1] = 0  

    
    sa, sb = clean_wind[1]

    
    for x in range(sa + 1, R - 1):  
        room[x][0] = room[x + 1][0]
    for y in range(0, C - 1):  
        room[R - 1][y] = room[R - 1][y + 1]
    for x in range(R - 1, sa, -1):  
        room[x][C - 1] = room[x - 1][C - 1]
    for y in range(C - 1, 1, -1): 
        room[sa][y] = room[sa][y - 1]
    room[sa][1] = 0  

def main(T):
    dust = []

    while T:
        for i in range(R):
            for j in range(C):
                if room[i][j] != -1 and room[i][j] != 0:
                    dust.append((i, j))
        spread()
        wind()
        T -= 1
main(T)

result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1 and room[i][j] != 0:
            result += room[i][j]

print(result)


    