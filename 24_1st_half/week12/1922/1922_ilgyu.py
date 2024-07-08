import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input()) # 간선의 수

info = []
parent = [i for i in range(n+1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    info.append((cost, s, e)) # 오름차순 정렬하려고 cost를 튜플의 첫번째로

info.sort()
# 오름차순 정렬을 튜플 + sort()로 하든지
# lamda로 하든지

# print(info)
# print(parent)

# 1. 부모찾기 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 2. 합치기
def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(x, y):
    return find_parent(x) == find_parent(y)

ans = 0
for cost, s, e in info:
    if not same_parent(s, e):
        union_parent(s, e)
        ans += cost

print(ans)