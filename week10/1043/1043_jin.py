from sys import stdin

input = stdin.readline


N, M = map(int, input().split())  # 사람 수 / 파티 수
T = int(input())                  # 진실 아는 사람 수
for _ in range(M):

