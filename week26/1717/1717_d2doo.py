# 집합의 표현
from sys import setrecursionlimit
setrecursionlimit(100000)

def find(x): # 재귀로 타고 들어가면서 진짜 부모 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a) # a의 부모를 찾고
    b = find(b) # b의 부모를 찾아서
    if a < b: # 더 작은 값을 부모로 해주기
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)] # n + 1개의 집합

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")