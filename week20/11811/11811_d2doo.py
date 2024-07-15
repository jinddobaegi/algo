# 데스스타
# 비트마스킹
# 행열[i][j]는 수열[i] and 수열[j]값

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not i == j: # 광선검에 의해 볼 수 없는 부분 빼고
            # and 조건으로 1이 켜져있다는건 일단 그 자리는 무조건 1이 켜져있단 뜻
            ans[i] = ans[i] | arr[i][j]
        else:
            continue

print(*ans)