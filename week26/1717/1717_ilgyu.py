import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x): # 부모찾는 함수
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    # 작은애를 부모로
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")