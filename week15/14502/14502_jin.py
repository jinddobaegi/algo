from sys import stdin

input = stdin.readline

# 바이러스는 상하좌우로 퍼짐
# 세 칸에 벽을 세워서 만들 수 있는
# 안전영역의 최대 크기

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

