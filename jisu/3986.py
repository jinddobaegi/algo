T = int(input())
cnt = 0

for i in range(T):
    word = input()
    stack = []
    for j in word:
        if stack and stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)
    if not stack:
        cnt += 1

print(cnt)
