import sys
sys.stdin = open('week11/1197/1197.txt')
input = sys.stdin.readline

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 - find_parent(parent, node2)

    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2



totalnode, totalline = map(int, input().split())
parent = [0] * (totalnode+1)
for i in range(1, totalnode+1):
    parent[i] = i

# print(parent)

lines = []
shortestsum = 0

for _ in range(totalline):
    node1, node2, weight = map(int, input().split())
    lines.append((weight, node1, node2))

lines.sort()

# print(lines)

for line in lines:
    weight, node1, node2 = line
    if find_parent(parent, node1) != find_parent(parent, node2):
        union_parent(parent, node1, node2)
        shortestsum += weight

print(shortestsum)

    
