# 트리 순회
# 실버1

import sys

# 전위 / 중위 / 후위 순회 값 출력 ㄱ

# 노드 개수 / 노드는 A부터 ~
N = int(input())
# tree = []  리스트로 하니까 안 되더라..
tree = {}
for _ in range(N):
    # 노드, 왼쪽 자식, 오른쪽 자식 (자식 없으면 .으로 표시)
    n, l, r = input().rstrip().split()
    tree[n] = [l, r]   # 그 노드에 왼오 자식 노드 담아

    # 전위 순회(루트부터 & 왼쪽부터 슥삭)
    def jeon(n):
        if n != '.':
            print(n, end="") # 뿌리
            jeon(tree[n][0]) # 왼
            jeon(tree[n][1])# 오


    # 중위 순회(왼 루 오)
    def joong(n):
        if n != '.':
            joong(tree[n][0]) # 왼
            print(n, end='') # 뿌
            joong(tree[n][1]) # 오


    # 후위 순회(왼 오 루)
    def hoo(n):
        if n != '.':
            hoo(tree[n][0]) # 왼
            hoo(tree[n][1]) # 오
            print(n, end='') # 뿌



# 출력
jeon('A')
print()
joong('A')
print()
hoo('A')



