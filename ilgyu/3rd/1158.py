import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

circle = [i for i in range(1, n+1)]
stack = []
i = 0

while circle:
    i = (i + k - 1) % len(circle)
    num = circle.pop(i)
    stack.append(num)

print("<", end="")
print(", ".join(map(str, stack)), end="")
print(">")

