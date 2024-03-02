# 좋은 단어
# 실버 4

import sys

n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    stack = []

    for i in range(len(s)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1
print(cnt)