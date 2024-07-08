import sys
sys.stdin = open('input.txt')

def find(x):
    # 루트노드인 경우
    if parent[x] == x:
        return x
    # 루트노드가 아닌 경우 루트노드를 찾을 때까지 재귀적으로 호출
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

n, m = map(int, input().split())
known = list(map(int, input().split()))
if known[0] > 0:
    known_truth = set(known[1:])
else:
    known_truth = set()

parent = list(range(n + 1))
# print(parent)
# 진실을 아는 사람들을 하나의 그룹으로 묶기
truth_root = 0 # 0번을 가상의 루트 노드로 설정해서 여기다가 진실을 아는 사람을 다 묶음
for person in known_truth:
    union(truth_root, person)

parties = [] # 전체 파티의 집합
# 여기서 예제에서  2 3 4 이렇게 주어지면 이게 2번파티가 아니라 그냥
# 임의의 파티에 2명, 3번과 4번 사람이 참가한다는 뜻
for _ in range(m):
    party = list(map(int, input().split()[1:]))
    print(party)
    parties.append(party)
    # 파티 참가자를 하나의 그룹으로 묶기
    for person in party:
        union(party[0], person)
# print(parties)
# 거짓말을 할 수 있는 파티 수 계산
answer = 0
# 위에서
# 1. 진실을 아는 사람들을 하나의 그룹으로 묶었고
# 2. 파티에  참가한 사람들을 하나로 묵었으니까
# 각 파티를 돌면서( 파티를 돈다는게 임의의 파티들에 참가한 사람들의 번호를 확인)
# 그 파티에 참가한 사람의 루트노드가 진실을 아는 사람의 루트노드와 다르면(즉 0이 아니면)
# 카운트 + 1
for party in parties:
    if find(party[0]) != find(truth_root):
        answer += 1

print(answer)






# 실패

# n, m = map(int, input().split()) # 사람수, 파티의 수
# true_info = list(map(int, input().split()))
#
# know_true = true_info[1:]
# # 파티에 오는사람 수, 각각의 번호
# party_info = [[] for _ in range(m+1)]
# for i in range(m):
#     each_info = list(map(int, input().split()))
#     party_info[i+1].append(each_info[1:])
# # print(know_true)
# print(party_info)
# print(know_true)
# # 진실을 아는 사람이 없으면 = know_true의 길이가 1
# # 전체 파티의 수가 정답
# total = m
# if true_info[0] == 1:
#     print(total)
#
# # 아니면
# # 각각의 파티를 돌면서 각 요소에 know_true가 있는지 검사
# else:
#     for i in range(1, m+1):
#         for num in party_info[i][0]:
#             print('검사할 번호:', num)
#             if num in know_true:
#                 total -= 1
#                 print('여기서 한번 뺌')
#                 break
# print(total)
# # [10] 이후에 [3, 10] 이 있으면 이경우도 카운트 해줘야함 ..
#
