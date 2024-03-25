import sys
sys.stdin = open('input.txt')

N = int(input())
tree = {}

# 트리문제는 트리를 dic형태로 만들어서 하는듯

for n in range(N):
    root, left, right = map(str, input().split())
    # root, left, right = sys.stdin.readline().strip().split() 이렇게 입력하는 거 알아보기
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

preorder('A')
print()
inorder('A')
print()
postorder('A')