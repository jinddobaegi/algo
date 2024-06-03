arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = 1e9

def dfs(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return

    if x >= 10:   # x가 10 이상이면 다음 줄로 이동
        dfs(0, y+1, cnt)
        return

    if arr[x][y] == 1:   # 1이면 색종이들 사이즈별로 붙여보기
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            temp = 0
            # 색종이 붙일 수 있는지 확인
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if arr[i][j] == 0:
                        temp = 1
                        break
                if temp:
                    break

            # 색종이 붙이기
            if not temp:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        arr[i][j] = 0

                paper[k] += 1
                dfs(x+k+1, y, cnt+1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        arr[i][j] = 1

    else:
        dfs(x+1, y, cnt)

dfs(0, 0, 0)
if ans == 1e9:
    print(-1)
else:
    print(ans)