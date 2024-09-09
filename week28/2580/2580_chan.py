import sys
sys.stdin = open("week28/2580/2580.txt")
input = sys.stdin.readline

# 스도쿠 1부터 9까지의 숫자로 이루어져야한다. 각줄과 3*3칸에 

board = [list(map(int, input().split()))for _ in range(9)]

# ------------------------------------------------------------
# 첫번째 풀이 실패(다시 채우기를 안해서 그런가봄)

# for i in board:
#     print(i)


# def cal_zone(number, i, j):
#     number_list = number.copy() 
#     start = (i // 3) * 3
#     start2 = (j // 3) * 3

#     for a in range(start, start + 3):
#         for b in range(start2, start2 + 3):
#             if board[a][b] in number_list:
#                 number_list.remove(board[a][b])

#     if number_list:
#         return number_list[0] 
#     else:
#         return -1 # 실패인건데....이렇게도 되나..?
                
# def check_switch(i, j):
#     delta = [-1, 1]
#     # 상하의 9개를 체크한다.
#     number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     # 상하
#     for a in range(9):
#         if board[a][j] in number:
#             number.remove(board[a][j])
#     # for a in range(0, i-1):
#     #     if board[a][j] in number:
#     #         number.remove(board[a][i])
#     #         # print(board[a][j])
#     # for b in range(i, 9):
#     #     if board[b][j] in number:
#     #         number.remove(board[b][j])
#     #         # print(board[b][j])
#     # 좌우
#     for b in range(9):
#         if board[i][b] in number:
#             number.remove(board[i][b])
#     # for a in range(0, j-1):
#     #     if board[i][a] in number:
#     #         number.remove(board[i][a])
#     # for b in range(j, 9):
#     #     if board[i][b] in number:
#     #         number.remove(board[i][b])

#     result = cal_zone(number, i, j)
#     # print(result)
#     return result
    
# for i in range(9):
#     for j in range(9):
#         if board[i][j] == 0:
#             num = check_switch(i, j)
#             board[i][j] = num

# for bo in board:
#     print(*bo)



# ------------------------------------------------------------------------------------------------------
# 두번째 풀이 실패(시간초과) 다른 방법을 모르겠네

# def switch(i, j, num):
#     flag = False

#     for a in range(9):
#         if board[i][a] == num:
#             return False
    
#     for b in range(9):
#         if board[b][j] == num:
#             return False
    
#     start = (i // 3) * 3 
#     start2 = (j // 3) * 3 # 0 3 6

#     for r in range(start, start + 3):
#         for c in range(start2, start2 + 3):
#             if board[r][c] == num:
#                 return False
    
#     return True


# def sudoku():
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 for num in range(1, 10):
#                     if switch(i, j, num) == True:
#                         board[i][j] = num
#                         if sudoku():
#                             return True
#                         board[i][j] = 0
#                 return False
#     return True

# sudoku()

# for bod in board:
#     print(*bod)


# ------------------------------------------------------------------------------------------------------
# 세번째 풀이...

empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(i, j, num):
    # 가로줄, 세로줄 검사
    for x in range(9):
        if board[i][x] == num or board[x][j] == num:
            return False
    
    # 3x3 박스 검사
    start_row, start_col = (i // 3) * 3, (j // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True


def sudoku(index):
    if index == len(empty_cells):
        return True

    i, j = empty_cells[index]
    for num in range(1, 10):
        if is_valid(i, j, num):
            board[i][j] = num
            if sudoku(index + 1):
                return True
            board[i][j] = 0
    return False

sudoku(0)

for bo in board:
    print(*bo)

# ------------------------------------------------------------------------------------------------------
# 네번쨰 풀이 

