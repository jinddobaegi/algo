# 스택
# 도저히 모르겠어ㅓㅅ 찾아봄
# 시작점 인덱스와 높이를 스택에 저장
# 탐색 시작하면서 스택에 최솟값에 대한 정보를 계속 유지
# 스택의 가장 위의 값보다 작은 값이 나온다면 그 값들을 pop하면서 넓이 구하기
# ...?
import sys
input = sys.stdin.readline

N = int(input())  # 가로 칸의 수
stack = []
h_lst = []
max_s = 0

for _ in range(N):
    h = int(input())  # 높이
    h_lst.append(h)

# for i in range(N):
#