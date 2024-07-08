import sys
sys.stdin = open("1991.txt")
# input = sys.stdin.readline

def front(node):
    if node != '.':
        print(node, end="")
        front(tree[node][0])
        front(tree[node][1])
def mid(node):
    if node != '.':
        mid(tree[node][0])
        print(node, end="")
        mid(tree[node][1])
def back(node):
    if node != '.':
        back(tree[node][0])
        back(tree[node][1])
        print(node, end="")


tree = {}
totalnode = int(input())
for _ in range(totalnode):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

root = 'A'

front(root)
print()
mid(root)
print()
back(root)