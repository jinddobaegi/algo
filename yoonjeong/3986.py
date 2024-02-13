N = int(input())
cnt = 0

for _ in range(N):
    w = list(input())
    stack = []

    for i in range(len(w)):
        if len(stack) == 0:
            stack.append(w[i])
        else:
            if w[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(w[i])

    if len(stack) == 0:
        cnt += 1

print(cnt)