# 달팽이

N = int(input()) # 홀수
find_num = int(input()) # 좌표를 찾아야하는 친구
i = N // 2
j = N // 2
arr = [[0] * N for _ in range(N)]
arr[i][j] = 1

move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위, 오, 아, 왼

# 규칙
# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6...
# if N == 가야하는 숫자 -1 이면? 3번
# 짝수일 때 위 오른쪽, 홀수일 떄 아래 왼쪽
cnt = 1
flag = 1

while flag:
    for di, dj in move:
        for _ in range(2):
            ni, nj = i + di, j + dj
            if 0 < ni < N and 0 < nj < N and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                # 갱신을 해줘
                i = ni
                j = nj
        cnt += 1