n = int(input())

cnt = 0
for _ in range(n):
    stack = []
    words = list(map(str, input()))
    for word in words:
        if len(stack) == 0 or stack[-1] != word:
            stack.append(word)
        else:
            stack.pop()
    if len(stack) == 0:
        cnt += 1
print(cnt)