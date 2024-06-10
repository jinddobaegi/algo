# 가르침

def teach(prev, cnt):
    global ans
    if cnt == K - 5:
        tmp = 0
        for word in words:
            flag = 0
            for w in word:
                if not letter[ord(w) - ord('a')]:
                    flag = 1
                    break
            if not flag:
                tmp += 1
        ans = max(ans, tmp)
        return
    for i in range(prev, 26):
        if not letter[i]:
            letter[i] = 1
            teach(i, cnt + 1) # 사실상 cnt == k - 5 될때까지 계속 실행
            letter[i] = 0

N, K = map(int, input().split()) # N개의 단어, 가르칠 수 있는 K개의 글자
words = []
for _ in range(N):  # 앞뒤 짤라먹고 필요한 단어만 꺼내
    words.append(input()[4:-4])

if K < 5: # 'anta', 'tica'로 시작하고 끝나는 남극단어를 배우기 위해선 [a, n, t, i, c] 5글자를 반드시 배워야만 함.
    print(0)
elif K >= 26: # 알파벳을 다 가르칠 수 있으면 단어 개수 출력하고 끝내기
    print(N)
else:
    ans = 0
    letter = [0] * 26
    # letter[0], letter[2], letter[8], letter[13], letter[19] = 1
    for i in ['a', 'n', 't', 'i', 'c']:
        letter[ord(i) - ord('a')] = 1
    teach(0, 0)
    print(ans)

# 순열을 쓸 수 있었더라면...
# 17번째 줄에서 알파벳을 모두 돌리는것이 아니라 words가 있으니까 그 안의 글자들만 튜플에 넣고 돌았어도 좋지 않았을까?