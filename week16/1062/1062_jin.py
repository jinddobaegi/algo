N, K = map(int, input().split())
words = list(input() for _ in range(N))

# K개의 글자를 가르쳤을 때
# 학생들이 읽을 수 있는 단어 개수의 최댓값 출력

# K개의 글자가 뭔지는 알 수 없음
# 따라서 가장 많이 읽을 수 있게 하는 경우 중
# 가르치는 글자가 K개 이하인 것 중에 가장 큰 경우를 고르면 됨
# 일단 뭔가 브루트포스 돌려도 될 것 같음


def check_func():
    # antic는 무조건 포함
    # 따라서 K < 5면 답은 0
    if K < 5:
        return 0

    max_v = 0

    for i in range(1 << N):
        combinations = []
        for j in range(N):
            if i & (1 << j):
                combinations.append(words[j])

        # 조합이 완성됨
        if not combinations:
            continue

        # combinations가 빈 리스트가 아닌 경우
        # 각 단어를 돌면서... 몇 개의 글자를 추가로 알아야 하는지 알아보자

        new_chars = 'antic'
        for word in combinations:
            for char in word:
                if char not in new_chars:
                    new_chars += char

        # 만약 글자의 길이가 K 이하라면
        # max_v의 조건에 맞춰 갱신
        if len(new_chars) <= K:
            max_v = max(max_v, len(combinations))

    return max_v

print(check_func())