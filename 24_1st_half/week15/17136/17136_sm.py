# 색종이 붙이기
# 골드2

# 문제
'''
정사각형 색종이 5종류 있음 - 각 5개씩 있음
10 * 10 종이 위에 붙이려고 함
1 적힌 칸은 색종이로 덮어야 함!
최소 색종이 개수 구하긔
'''

# 풀이법
'''
- 좌표로 접근해야할듯
- dfs 슛
'''

import sys
input = sys.stdin.readline

# 입력
square = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 0, 0, 0, 0]   # 색종이 개수

# # 중복값 막을라고 집합 쓴거
# res = set()

def dfs(x, y, cnt):
    global f

    if y >= 10:
        ret = min(f, cnt)
        return

    if x >= 10:
        dfs(0, y + 1, cnt)
        return

    if square[x][y]:
        for p in range(5):
            if paper[p] == 5: # 5개 다 쓰면 넘기고
                continue

            if x + p >= 10 or y + p >= 10: # 범위 넘어가면 pass
                continue
            flag = 0

            for i in range(x, x + p + 1):
                for j in range(y, y + p + 1):
                    if not square[i][j]: # 범위가 0이면
                        flag = 1
                        break
                if flag: break

            if not flag: # 0없으면 -> 1
                for i in range(x, x + p + 1):
                    for j in range(y, y + p + 1):
                        square[i][j] = 0

                paper[p] += 1

                # 최소인 것만 갱신하고 나머지는 원래대로
                dfs(x + p + 1, y, cnt + 1)
                paper[p] -= 1

                for i in range(x, x + p + 1):
                    for j in range(y, y + p + 1):
                        square[i][j] = 1
    else: # 1이 아니면 다음 x
        dfs(x + 1, y, cnt)

f = float('inf')
dfs(0, 0, 0)
if f == float('inf'):
    print(-1)
else:
    print(f)