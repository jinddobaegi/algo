N = int(input())
ans = []

def sol(cnt):
    for i in range(1, (cnt//2)+1):  # 인접한 두 수열이 동일한지 확인
        if ans[-i:] == ans[-2*i:-i]:
            return
    if cnt == N:  # 수열을 완성한 경우
        print("".join(ans))
        exit()
    for i in range(1, 4):
        ans.append(str(i))
        sol(cnt+1)
        ans.pop()

sol(0)