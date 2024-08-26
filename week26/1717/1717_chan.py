import sys
sys.stdin = open("week26/1717/1717.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

def find(x, parent):
    # if parent[x] != x:
    #     return find(parent[x], parent)
    # else: 
    #     return x
    if parent[x] != x:
        parent[x] = find(parent[x], parent)  # 경로 압축
    return parent[x]

def union(x, y, parent):
    parent[find(y, parent)] = find(x, parent)

parent = list(i for i in range(N+1))


def result(M, parent):
    for _ in range(M):
        k, a, b = map(int, input().split())
        if k == 0:
            union(a, b, parent)
        if k == 1:
            if find(a, parent) == find(b, parent):
                print("YES")
            else:
                print("NO")

result(M, parent)