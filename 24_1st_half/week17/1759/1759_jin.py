from sys import stdin

input = stdin.readline

# 서로 다른 L개의 알파벳
# 모음 한 개 이상
# 자음 두 개
# 알파벳은 오름차순
# 문자의 종류는 C가지
# 즉, C개 중 서로 다른 L개 선택

L, C = map(int, input().split())
letters = list(map(str, input().split()))  # C개
vowels = {'a', 'e', 'i', 'o', 'u'}
visited = [0] * C

letters.sort()


def dfs(i, cnt, word):
    if cnt == L:
        word_to_set = set(word)
        if (word_to_set & vowels) and len(word_to_set - vowels) >= 2:
            res.append(word)
        return

    if i == C:
        return

    if visited[i]:
        dfs(i+1, cnt, word)

    else:
        visited[i] = 1
        dfs(i+1, cnt+1, word+letters[i])

        visited[i] = 0
        dfs(i+1, cnt, word)


res = []
dfs(0, 0, '')

for pw in res:
    print(pw)