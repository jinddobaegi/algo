import sys
sys.stdin = open('week11/4386/4386.txt')
input = sys.stdin.readline

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)

    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

def length(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


totalnode = int(input())
parent = [[0] * (totalnode+1)for _ in range(totalnode+1)]

for i in parent:
    print(i)

for i in range(1, totalnode+1):
    parent[i] = i

nodes = []
sortestsum = 0



