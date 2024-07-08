import sys
input = sys.stdin.readline

N = int(input())
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)

# 아스키코드로 트리 만들어봄..
for _ in range(N):
    p, c1, c2 = input().split()

    p = (ord(p) - 64)
    if c1 == '.':
        c1 = None
    else:
        c1 = (ord(c1) - 64)

    if c2 == '.':
        c2 = None
    else:
        c2 = (ord(c2) - 64)

    ch1[p] = c1
    ch2[p] = c2

# 전위 순회
def preorder(p):
    if p:
        print(chr(p+64), end = '')
        preorder(ch1[p])
        preorder(ch2[p])

# 중위 순회
def inorder(p):
    if p:
        inorder(ch1[p])
        print(chr(p+64), end = '')
        inorder(ch2[p])

# 후위 순회
def postorder(p):
    if p:
        postorder(ch1[p])
        postorder(ch2[p])
        print(chr(p+64), end = '')


preorder(1)
print()
inorder(1)
print()
postorder(1)