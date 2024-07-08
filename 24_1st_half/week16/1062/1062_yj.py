import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().strip()[4:-4] for _ in range(N)]
learn = [0] * 26
ans = 0

# a,n,t,i,c 은 필수로 배워야 함
for i in 'antic':
    learn[ord(i) - ord('a')] = 1

def dfs(idx, cnt):
    global ans

    if cnt == K - 5:  # 문자 수를 다 채운 경우
        temp = 0
        for word in words:  # 각 단어 읽을 수 있는지 없는지 확인
            can_read = True
            for i in word:
                if not learn[ord(i) - ord('a')]:
                    can_read = False
                    break
            if can_read:
                temp += 1

        ans = max(ans, temp)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    dfs(0,0)
    print(ans)