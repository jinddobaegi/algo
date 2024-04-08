# F, S, G, U, D
# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
# use the stairs

import sys
sys.stdin = open('5014.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def go_floor(now, goal):
    global push
    if now < goal:
        push += 1
        go_floor(now+up, goal)
    elif now > goal:
        push += 1
        go_floor(now-down, goal)
    elif now == goal:
        print(push)
        return
    elif now > total_floor or now < 1:
        print('use the stairs')
        return
total_floor, now, goal, up, down = map(int, input().split())
push = 0
go_floor(now, goal)





