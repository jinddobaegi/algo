# 암호 만들기

# 모음 자음 개수 체크
def check(arr):
    v, c = 0, 0 # 모음 cnt, 자음 cnt(cardinal)
    for i in arr:
        if i in vowel:
            v += 1
        else:
            c += 1
    if v >= 1 and c >= 2:
        return 1
    else:
        return 0

def backtracking(arr):
    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < words[i]: # 오름차순
            arr.append(words[i])
            backtracking(arr)
            arr.pop() # 그 다음단계를 위해 pop

L, C = map(int, input().split()) # 암호 길이 L, 가진 알파벳 수 C
words = input().split() # a, t, c, i, s, w
words.sort() # a, c, i, s, t, w
vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(C - L + 1): # s 부터는 길이를 만족시키지 못함
    start = [words[i]]
    backtracking(start)