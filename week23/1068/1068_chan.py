import sys
sys.stdin = open("week23/1068/1068.txt")
input = sys.stdin.readline
from collections import defaultdict, deque

# # 트리 구조 생성
# def build_tree(parents):
#     tree = defaultdict(list)
#     root = -1
#     for child, parent in enumerate(parents):
#         if parent == -1:
#             root = child
#         else:
#             tree[parent].append(child)
#     return tree, root

# # 노드 삭제
# def delete_subtree(tree, delete_node):
#     nodes_to_delete = deque([delete_node - 1])
#     while nodes_to_delete:
#         current = nodes_to_delete.popleft()
#         nodes_to_delete.extend(tree[current])
#         del tree[current]

# # 리프 노드 찾기
# def count_leaf_nodes(tree, root):
#     if root not in tree:  # 루트 노드가 리프 노드인 경우
#         return 1
#     leaf_count = 0
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node not in tree or not tree[node]:  # 자식이 없는 노드가 리프 노드
#             leaf_count += 1
#         else:
#             stack.extend(tree[node])
#     return leaf_count

# # 입력 받기
# n = int(input())
# parents = list(map(int, input().split()))
# delete_node = int(input())

# # 트리 생성
# tree, root = build_tree(parents)

# # 노드 삭제
# if delete_node == root:
#     print(0)
# else:
#     delete_subtree(tree, delete_node)

#     # 리프 노드 개수 세기
#     leaf_count = count_leaf_nodes(tree, root)
#     print(leaf_count)

def build_tree(parents):
    tree = defaultdict(list)
    root = -1
    for child, parents in enumerate(parents):
        if parents == -1:
            root = child
        else:
            tree[parents].append(child)
    return tree, root

def delete_subtree(tree, delete_node):
    def dfs(node):
        for child in tree[node]:
            dfs(child)
        del tree[node]

    if delete_node in tree:
        dfs(delete_node)

    for root_num in list(tree):
        if delete_node in tree[root_num]:
            tree[root_num].remove(delete_node)

def count_leaf_nodes(tree, root):
    if root not in tree:  # 루트 노드가 리프 노드인 경우()``
        return 1
    leaf_count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in tree or not tree[node]:  # 자식이 없는 노드가 리프 노드
            leaf_count += 1
        else:
            stack.extend(tree[node])
    return leaf_count
    

N = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

tree, root = build_tree(parents)
if delete_node == root:
    print(0)
else:
    delete_subtree(tree, delete_node)
    leaf_count = count_leaf_nodes(tree, root)
    print(leaf_count)


