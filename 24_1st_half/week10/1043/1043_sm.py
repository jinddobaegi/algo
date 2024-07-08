# 그짓말
# 골드4

# 유니온 파인드
# union (서로 다른 두개 집합을 하나의 집합으로 병합하는 연산 aka. 합집합)
# -> 한마디로 노드를 합치는 연산
# find (하나인 원소가 어떤 집합에 속해있는지 찾기, 판단하기)
# -> 한마디로 노드의 루트 노드를 찾는 연산


# 문제
# 사람의 수 N이 주어진다.
# 그리고 그 이야기의 진실을 아는 사람이 주어진다.
# 그리고 각 파티에 오는 사람들의 번호가 주어진다.
# 지민이는 모든 파티에 참가해야 한다.
# 지민이가 거짓말쟁이로 알려지지 않으면서,
# 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# import sys
#
# # find : 루트 노드 찾는 함수
# def find(x, parent):
#     # 만약에 자기 부모 노드면
#     if parent[x] != x:
#         parent[x] = find(parent[x], parent) # 재귀로 부모노드 따라가면서 루트 노드 찾는거
#     return parent[x]
#
#
# # union : 두 원소가 속합 집합 합치기
# def union(a, b, parent):
#     # 각자의 루트 노드 찾고, 그게 이제 그 값이 속한 집합의 대표인거
#     a = find(a, parent)
#     b = find(b, parent)
#     # 더큰 번호 루트 노드 가진 집합의 부모를 더 작은 번호의 루트노드로 설정하자
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# ------------ 솔직히 여기까지는 유니온 파인드 함수 그대로 쓰는거라서 어찌저찌 썼긴 함
# 이 다음부터가 문제

# N 사람 수: 노드의 개수 / M 파티 수 : 간선의 개수
# N, M = map(int, input().split())
# truth = [*map(int, input().split())]
# people = truth[0] # 진실 아는 사람 수
# people_num = truth[1:] # 진실 아는 사람 번호 리스트

# 진실을 아는 사람의 수 / 번호
# 일단 input받는 것부터 좀 까다롭;
# input_lst = list(map(int, input().split()))
# 진실 아는 사람의 수
# person_num = input_lst[0]
# 진실을 아는 사람의 번호  {1, 2, 7}
# truth_number = set(input_lst[1:])


#--------------------------------------------------------------------

import sys
input = sys.stdin.readline

# find : 루트 노드 찾는 함수
def find(x):
    # 본인이 부모노드의 값과 같으면
    if x == parents[x]:
        return x
    # 재귀로 부모노드 따라가면서 루트 노드 찾는거
    return find(parents[x])


# union : 두 원소가 속합 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())
# 각자의 부모노드를 본인으로 초기 설정해주고
parents = [i for i in range(n+1)]

for i in list(map(int, input().split()[1::])):
    parents[i] = 0

party = []
for _ in range(m):
    people = list(map(int, input().split()[1:]))
    party.append(people)
    if len(people) > 1:
        for i in range(1, len(people)):
            union(people[i-1], people[i])

cnt = 0
for p in party:
    for person in p:
        if find(parents[person]) == 0:
            break
    else:
        cnt += 1

print(cnt)
