# 행렬
# 이게 그리디임? 

# 뒤집기 함수
def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0

N, M = map(int, input().split()) 

A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
cnt = 0

if (N < 3 or M < 3) and A != B: # 리스트의 크기가 3x3이 되지 않으면  
    cnt = -1 # 뒤집을 수 없다.
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                cnt += 1
                check(i, j)

if cnt != -1:
    if A != B: # A와 B가 같지 않으면
        cnt = -1
print(cnt)