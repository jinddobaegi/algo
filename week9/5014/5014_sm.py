# 스타트 링크
# 실버1

# 문제
# 늦게 도착하고 말았다.
# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크 위치는 G층이다.
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
# 보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다.
# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다.
# (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

# 전략-----------------------------------------------------------------------------
# BFS로 엘베 이동하며 체크해주기


import sys
from collections import deque
# 입력
# F층으로 이루어진 고층 건물
# G -> 스타트링크 층수
# S -> 현재 위치
# U 위로 U층  # D 아래로 D층
F, S, G, U, D = map(int, sys.stdin.readline().split())

# 횟수 체크용 배열
check = [0 for _ in range(F+1)]

# 버튼 누른 횟수
move = 0

def bfs():
    global move
    q = deque()
    q.append(S)   # 엘베 출발점 큐에 넣긔
    check[S] = 1  # 시작층에 해당하는 횟수 체크하는 배열의 인덱스에 1 저장
    # q가 비어있지 않는 동안은 계속 반복문
    while q:
        stair = q.popleft()   # 맨 왼쪽 요소 뽑아서 현재 엘베 위치 지정
        if stair == G:   # 스타트링크에 도착했으면
            move = 1  # 이동을 했다고 체크하고
            # G에 도착했을 때 이동횟수 출력 (현재층까지 이동한 횟수에서 1뺀 것이 목표층까지 최소이동횟수)
            print(check[stair]-1)
            break # 목표층 가면 멈춰!
        # 엘베가 이동하는 동안 반복
        for i in (U, -D):
            next = stair + i
            # 다음층이 건물 층수 안에 있고 처음 방문하는 거면
            if 1 <= next <= F and check[next] == 0:
                check[next] = check[stair] + 1  # 현재 층 이동횟수에 +1
                q.append(next)  # 새로운 층 큐에 추가해주고 다음반복에서 탐색하게 만들긔

# 출력
bfs()
# 못 가면 use the stairs 출력
if move == 0:
    print("use the stairs")

