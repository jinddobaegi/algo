import sys
sys.stdin = open('input.txt')

# 시간초과 코드
# # 특정 위치에 특정 크기의 색종이를 놓을 수 있는지 확인하는 함수
# def can_place(paper, x, y, size):
#     # 색종이가 격자를 벗어나는지 확인
#     if x + size > 10 or y + size > 10:
#         return False
#
#     # 색종이가 1로만 이루어져 있는지 확인
#     for i in range(size):
#         for j in range(size):
#             if paper[x+i][y+j] != 1:
#                 return False
#     return True # 색종이를 놓을 수 있다는 것
#
# # 색종이를 놓거나 제거하는 함수
# def place_paper(paper, x, y, size, value):
#     for i in range(size):
#         for j in range(size):
#             paper[x+i][y+j] = value
# # place_paper(paper, 2, 3, 2, 0) 는 2x2크기의 색종이를 (2, 3)위치에 놓음
# # value가 0이면 색종이를 놓는경우 (기존 1을 0으로 바꿈 = 색종이를 놨다는 뜻)
# # value가 1이면 색종이를 제거 (0에서 다시1로 만들어줌 )
#
#
# # 백트래킹을 이용하여 문제를 해결하는 함수
# def solve(paper, used, x, y): # used는 현재까지 사용한 색종이의 수
#     global answer
#
#     # y가 10이 되면 모든 줄을 다 검사한 것이므로 최소 값을 갱신
#     if y == 10:
#         answer = min(answer, used)
#         return
#
#     # x가 10이되면 다음 줄로 넘어감
#     if x == 10:
#         solve(paper, used, 0, y+1)
#         return
#
#     # 현재 위치의 값이 0이면 다음 칸으로 넘어감
#     if paper[x][y] == 0: # 값이 1인 칸에만 색종이를 붙여야 하니까
#         solve(paper, used, x+1, y)
#         return
#
#     # 크기가 큰 색종이부터 놓아본다
#     for size in range(5, 0, -1):
#         if can_place(paper, x, y, size) and count[size] > 0:
#             # 색종이를 놓음
#             place_paper(paper, x, y, size, 0)
#             count[size] -= 1
#             # 다음 단계로 진행
#             solve(paper, used + 1, x + 1, y)
#             # 색종이를 제거하고 상태를 복구
#             place_paper(paper, x, y, size, 1)
#             count[size] += 1
#
# # 입력받기
# paper = [list(map(int, input().split())) for _ in range(10)]
# # 각 크기별 색종이 개수 초기화
# count = [0, 5, 5, 5, 5, 5]
# # 정답을 무한대로 초기화
# answer = float('inf')
# # 백트래킹 함수 호출
# solve(paper, 0, 0, 0)
#
# # 결과 출력
# print(answer if answer != float('inf') else -1)

# 위에는 시간초과 나옴
def can_place(paper, x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if paper[x + i][y + j] != 1:
                return False
    return True

def place_paper(paper, x, y, size, value):
    for i in range(size):
        for j in range(size):
            paper[x + i][y + j] = value

def solve(paper, used, x, y):
    global answer

    # 현재까지 사용한 색종이 개수가 최소값을 초과하면 종료
    # 이거 안 쓰면 시간초과 남
    if used >= answer:
        return

    if y == 10:
        answer = min(answer, used)
        return
    if x == 10:
        solve(paper, used, 0, y + 1)
        return
    if paper[x][y] == 0:
        solve(paper, used, x + 1, y)
        return

    for size in range(5, 0, -1): # 이거 1부터 5로 가도 됨
        if count[size] > 0 and can_place(paper, x, y, size):
            place_paper(paper, x, y, size, 0)
            count[size] -= 1
            solve(paper, used + 1, x + 1, y)
            place_paper(paper, x, y, size, 1) # 이부분이 백트래킹 다시 원래상태로 되돌려 놓음
            count[size] += 1

paper = [list(map(int, input().split())) for _ in range(10)]
count = [0, 5, 5, 5, 5, 5]
answer = float('inf')

solve(paper, 0, 0, 0)
print(answer if answer != float('inf') else -1)

