def work(x, y, cnt):
    global ans

    # 행 범위를 벗어나면 제일 작은 종이 수 리턴
    if y >= 10:
        ans = min(ans, cnt)
        return

    # 열 범위를 벗어나면 다음 행으로 가기
    if x >= 10:
        work(0, y+1, cnt)
        return

    # 만약 붙여야하는 곳이면
    if big_paper[x][y] == 1:
        # 붙여
        for k in range(4, -1, -1):
            # 종이를 5장 이상 사용하게 되는 경우
            if attach_paper[k] == 5:
                continue
            # 종이를 덮었을 때 크기가 넘치는 경우
            if x + k >= 10 or y + k >= 10:
                continue

            # 종이를 덮었는데 0인 칸이 있는 경우
            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if big_paper[i][j] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break

            # 여기서부터 쓸 수 있는 종이일 때의 풀이
            if flag == 0:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        big_paper[i][j] = 0 # 더이상 탐색하지 않게 0으로 바꿔주기

                attach_paper[k] += 1
                work(x + k + 1, y, cnt + 1)
                attach_paper[k] -= 1 # 다른 종이 사용했을 때의 경우도 보기위해서 다시 감소시켜주기

                # 여기 이해안감
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        big_paper[i][j] = 1
    else:
        work(x + 1, y, cnt)


big_paper = [list(map(int, input().split())) for _ in range(10)]
attach_paper = [0 for _ in range(5)] # 종이 사용량

ans = 1e7
work(0, 0, 0)

if ans == 1e7:
    print(-1)
else:
    print(ans)