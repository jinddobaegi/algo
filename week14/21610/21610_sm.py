# 마법사 상어와 비바라기
# 골드5

# 문제
'''
비바라기 시전하면 비구름 만들어짐
 근데 비바라기 크기 N * N
 격자 칸에는 바구니 하나 有 = 칸 전체
 바구니 저장가능한 물 양 제한 x
 (r,c) = r행 c열에 있는 바구니
 A[r][c] = (r,c)에 있는 물의 양
'''


'''
< 우리가 진행해야 할 과정 >
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
   물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 
   (r, c)에 있는 바구니의 물이 양이 증가한다.
    - 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    - 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, 
      (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
   이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
'''

# 로직
# 아 이거 문제 이해가 일단 잘 안됩니다..
# 뭔가 풍선팡처럼 하면 될 것 같은데..
# 구현 문제


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int,input().split())) for i in range(n)]
move = []
for i in range(m):
    # 구름이 d 방향으로 s칸 이동한다
    d, s = map(int, input().split())
    move.append([d,s])

# 초기 구름 위치를 잡아주고
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

# 일단 풍선팡처럼 방향을 설정한다
# 근데 얘는 방향이 8개야...
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 1. 구름 이동
# 구름이 m번 이동함
for i in range(m):
    x,y = move[i]
    next = []
    # for cloud in clouds:
        # 블로그 찾아보니까 여기서 모듈러 연산한다고 하는데 그 코드부터 이해가 안가네요..
