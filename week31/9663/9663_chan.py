import sys
sys.stdin = open("week31/9663/9663.txt")
from itertools import product, combinations

# queens = int(input())

# chess_board = [[False]* queens for _ in range(queens)]
# dp = [[-1]* queens for _ in range(queens)]

# 포문으로 돌리고 
# 방향마다 true로 표시하고 이미 true이면 그부분은 종료시킨다.
# queens의 개수만큼 퀸이 배치됬다면
# 종료시키고 카운트를 증가 시킨다.
# 퀸을 배치할때의 경우의 수를 구해야하기 때문에 재귀로 할까???

# def check_attack(board, r, c):
#     delta = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]

#     for dr, dc in delta:
#         for long in range(queens):
#             nr, nc = r + (long * dr), c + (long * dc)
#             if 0 <= nr < queens and 0 <= nc < queens:
#                 if board[nr][nc]:
#                     return False
#     return True
    

# def queen_move(board, row, count):# 상하좌우대각선

#     if count == queens:
#         return 1
    
#     placement = 0
#     for col in range(queens):
#         if check_attack(board, row, col):
#             board[row][col] = True
#             placement += queen_move(board, row + 1, count + 1)
#             board[row][col] = False

#     return placement




# print(queen_move(chess_board, 0, 0))
                 

queens = int(input())

# 열과 대각선 체크를 위한 배열
col_check = [False] * queens
diag1_check = [False] * (2 * queens - 1)  # 왼쪽 대각선 (r - c가 같음)
diag2_check = [False] * (2 * queens - 1)  # 오른쪽 대각선 (r + c가 같음)

def queen_move(row, count):
    if count == queens:
        return 1
    
    placement = 0
    for col in range(queens):
        if not col_check[col] and not diag1_check[row - col] and not diag2_check[row + col]:
            # 퀸을 놓음
            col_check[col] = diag1_check[row - col] = diag2_check[row + col] = True
            placement += queen_move(row + 1, count + 1)
            # 퀸을 제거 (백트래킹)
            col_check[col] = diag1_check[row - col] = diag2_check[row + col] = False

    return placement

# 시작 행에서 퀸을 배치
print(queen_move(0, 0))
