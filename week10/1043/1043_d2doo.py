# 거짓말
# union-find ^^
# 노드를 합치고(union) 부모를 찾아(find) 서로소 집합을 찾아낸다?

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]


# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know):
    a = find(parent, a)
    b = find(parent, b)

    if a in know and b in know: # 둘 다 아는 사람이면 돌아가
        return

    if a in know: # a가 알면 b의 자리에 부모노드로 a를 넣어줘
        parent[b] = a

    elif b in know: # b가 알면 b를 a자리에 넣어줘
        parent[a] = b

    else: # 둘 다 아니면 숫자의 크기에 넣어줘(이게 이해가 안감)
        if a < b:
            parent[b] = a

        else:
            parent[a] = b


N, M = map(int, input().split())
know = list(map(int, input().split()))[1:] # for문 안돌리고 0번 인덱스에 있는 아는 사람의 숫자 재끼고 저장

parties = []
parent = list(range(N + 1)) # 각자의 부모노드 일단 본인으로 저장
# print(f'parent {parent}')

for _ in range(M):
    party_info = list(map(int, input().split())) # party를 저장받음
    party_len = party_info[0] # 첫번째는 인원
    party = party_info[1:] # 그 이후부터는 있는 사람 인덱스

    for i in range(party_len - 1): # 한 명일 땐 돌지 않게 하기 위해서
        union(parent, party[i], party[i + 1], know)

# -------------------------- 여기서 부터 이해가 완벽하게 안돼 ------------------------------
    parties.append(party)

ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know:
            break

    else:
        ans += 1

print(ans)